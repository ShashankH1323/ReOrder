import pandas as pd
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

def analyze_ab_test(csv_path):
    df = pd.read_csv(csv_path)
    
    # Calculate conversion rates
    control = df[df['experiment_group'] == 'Control (A)']
    variant = df[df['experiment_group'] == 'Variant (B)']
    
    c_conv = control['converted'].sum()
    c_total = len(control)
    c_rate = c_conv / c_total
    
    v_conv = variant['converted'].sum()
    v_total = len(variant)
    v_rate = v_conv / v_total
    
    print(f"Control Conversion Rate: {c_rate * 100:.2f}%")
    print(f"Variant Conversion Rate: {v_rate * 100:.2f}%")
    print(f"Relative Lift: {((v_rate - c_rate) / c_rate) * 100:.2f}%\n")
    
    # Statistical Significance (Two-sample proportion Z-test)
    pooled_prob = (c_conv + v_conv) / (c_total + v_total)
    se = np.sqrt(pooled_prob * (1 - pooled_prob) * (1/c_total + 1/v_total))
    z_score = (v_rate - c_rate) / se
    p_value = norm.sf(abs(z_score)) * 2 # two-sided
    
    print(f"Z-Score: {z_score:.3f}")
    print(f"P-Value: {p_value:.4f}")
    
    if p_value < 0.05:
        print("Result: STATISTICALLY SIGNIFICANT. The Variant outperformed the Control.")
    else:
        print("Result: NOT STATISTICALLY SIGNIFICANT. We cannot reject the null hypothesis.")
        
    # Visualizing Lift
    labels = ['Control', 'Variant']
    rates = [c_rate * 100, v_rate * 100]
    
    plt.bar(labels, rates, color=['#9E9E9E', '#2196F3'])
    plt.ylabel('Reorder Conversion Rate (%)')
    plt.title('A/B Test Results: One-Click Reorder')
    for i, v in enumerate(rates):
        plt.text(i, v - 1, f"{v:.1f}%", ha='center', color='white', fontweight='bold')
    plt.savefig('ab_test_results.png')

if __name__ == "__main__":
    analyze_ab_test('data/ab_test_results.csv')
