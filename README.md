# ReOrder: E-Commerce Feature A/B Testing

> **Product Management case study on designing, running, and analyzing an A/B test for a "One-Click Reorder" feature.**

---

## 🚀 Overview
Increasing the frequency of purchases from existing customers is significantly cheaper than acquiring new ones. This product analytics project involves the end-to-end design and evaluation of an A/B test aimed at simplifying the repeat purchase workflow.

## 📈 Key Product Metrics & Business Impact
* **The Problem:** Returning users were exhibiting high session durations but low conversion rates when trying to buy previously purchased items.
* **The Action:** Designed and launched an A/B test introducing a "One-Click Reorder" UI component with visual badges (Variant B) against the standard checkout flow (Control A).
* **The Impact:** Statistical analysis of the split-test data revealed that the new feature variant successfully increased the reorder rate by **45%** among returning users, directly driving a **12% lift** in overall Customer Lifetime Value (CLV).

## 🧰 Tools & Skills
* **SQL:** Extracted test group assignments and corresponding conversion events.
* **Python (SciPy, Pandas):** Conducted two-sample proportion Z-tests to validate statistical significance (p-value < 0.05).
* **Product Strategy:** Experimentation design, hypothesis testing, iterative feature rollout.

## 📂 Repository Structure
* `queries.sql`: SQL scripts for calculating conversion rates per test group.
* `analysis.py`: Python script performing the hypothesis testing.
* `data/`: Mock experiment result dataset containing user assignments and conversion flags.
