python
import pandas as pd
import matplotlib.pyplot as plt

# Load demographic dataset
demographic_data = pd.read_csv('Small_Business_Demographics_and_Performance.csv')

# Load trading dataset
trading_data = pd.read_excel('Trading Summary by Investor Type - Jan 2020 - Nov 2025_0.xlsx')

# Example analysis: Identify top growth industries
growth_industries = demographic_data.groupby('Industry')['Growth Rate'].mean().sort_values(ascending=False)
print("Top growth industries:")
print(growth_industries.head())

# Example analysis: Trading volume trend
trading_volume_trend = trading_data.groupby('Year')['Buy Volume'].sum()

# Plotting trading volume trend
plt.figure(figsize=(10, 6))
plt.plot(trading_volume_trend.index, trading_volume_trend.values, marker='o')
plt.title('Annual Trading Volume Trend')
plt.xlabel('Year')
plt.ylabel('Total Buy Volume')
plt.grid(True)
plt.show()
