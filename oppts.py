import pandas as pd
import matplotlib.pyplot as plt

# Load and clean data
file_path = "2024oppts.csv"
data = pd.read_csv(file_path)

# Convert currency strings to numeric values
data['emac'] = data['emac'].str.replace(',', '').replace('', '0').astype(float)
data['init_contract'] = data['init_contract'].str.replace(',', '').replace('', '0').astype(float)

# Calculate profit and filter valid data
data['profit'] = data['init_contract'] - data['emac']
valid_data = data[data['profit'].notna()].copy()

# Prepare for plotting
valid_data['oppt_num'] = valid_data['oppt_num'].astype(str)  # Convert to string for better labeling
grouped_data = valid_data.groupby('oppt_num')[['init_contract', 'emac', 'profit']].mean()
grouped_data = grouped_data.sort_values('profit', ascending=False)

# Create figure with proper sizing
plt.figure(figsize=(12, 6))

# Plot grouped bar chart
x = range(len(grouped_data))
width = 0.35
plt.bar(x, grouped_data['init_contract'], width, label='Initial Contract', color='blue')
plt.bar([i + width for i in x], grouped_data['emac'], width, label='EMAC', color='orange')

# Add profit line
plt.plot([i + width/2 for i in x], grouped_data['profit'], 'r-', label='Profit (Difference)')

# Formatting
plt.title('Profitability Comparison by Opportunity Number')
plt.xlabel('Opportunity Number')
plt.ylabel('Amount ($)')
plt.xticks([i + width/2 for i in x], grouped_data.index, rotation=45)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show plot (VS Code specific)
plt.show()
