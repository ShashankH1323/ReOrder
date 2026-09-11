-- Assign users to Control or Variant (Simulated query for extraction)
WITH experiment_assignments AS (
    SELECT 
        user_id,
        experiment_group,
        assignment_date
    FROM ab_test_assignments
    WHERE experiment_id = 'EXP_ONE_CLICK_REORDER'
),

-- Find out if they converted (purchased) within 7 days of assignment
conversions AS (
    SELECT 
        e.user_id,
        e.experiment_group,
        CASE WHEN p.purchase_id IS NOT NULL THEN 1 ELSE 0 END AS converted,
        p.revenue
    FROM experiment_assignments e
    LEFT JOIN purchases p 
      ON e.user_id = p.user_id 
     AND p.purchase_date >= e.assignment_date 
     AND p.purchase_date <= DATEADD(day, 7, e.assignment_date)
)

-- Aggregate Results
SELECT 
    experiment_group,
    COUNT(user_id) as total_users,
    SUM(converted) as total_conversions,
    ROUND(SUM(converted) * 100.0 / COUNT(user_id), 2) as conversion_rate,
    ROUND(AVG(revenue), 2) as average_revenue_per_user
FROM conversions
GROUP BY experiment_group;
