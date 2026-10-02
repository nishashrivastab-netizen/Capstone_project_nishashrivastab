
import pandas as pd
import matplotlib.pyplot as plt
import os
"""Task 10 — Outlier-corrected time series"""

# Select the first five rows of the order_date column to inspect its existing layout
raw_date_preview = merged_df[['order_id', 'order_date']].head()

# Display the raw date preview in a clean interactive grid table format
raw_date_preview

# Convert order_date to datetime type to enable time operations
merged_df['order_date'] = pd.to_datetime(merged_df['order_date'])

# Extract the YYYY-MM format from order_date and save it into a new column
merged_df['year_month'] = merged_df['order_date'].dt.strftime('%Y-%m')

# Display the first five rows of the new column to verify the change in grid format
merged_df[['order_id', 'order_date', 'year_month']].head()

# Group data by year_month and sum the order values including all rows
series_inc = merged_df.groupby('year_month')['order_value'].sum().round(2).reset_index()
series_inc.columns = ['Year-Month', 'Total (With Outliers)']

# Display the monthly summary grid to verify the calculations with outliers
series_inc

# Filter dataset to exclude the two outlier rows and calculate monthly sum
series_exc = merged_df[merged_df['is_outlier'] == False].groupby('year_month')['order_value'].sum().round(2).reset_index()
series_exc.columns = ['Year-Month', 'Total (Without Outliers)']

# Display the monthly summary grid to verify calculations after correction
series_exc

# Merge both calculated time series together into a single comparison grid frame
time_series_final = series_inc.merge(series_exc, on='Year-Month')

# Display the merged final time series comparison data in a clean grid format
display(time_series_final)

# Print the mandatory text paragraph detailing the genuine peak month shift explanation
print("\nTime Series Analysis Note:")
print("January's apparent lead is an artifact of the two bulk orders landing in January "
      "(00011 on 2026-01-28, 00098 on 2026-01-10), and that March is the genuine peak month "
      "once they're excluded — this is the whole point of doing Task 6 before Task 10, not after.")

"""Task 11 — Two visualizations (analysis/visualize.py)"""

# Calculate the return rates grouped by payment method in descending order
chart1_data = merged_df.groupby('payment_method')['returned'].mean().reset_index()
chart1_data['returned'] = (chart1_data['returned'] * 100).round(1)
chart1_data = chart1_data.sort_values(by='returned', ascending=False).reset_index(drop=True)
chart1_data.columns = ['Payment Method', 'Return Rate (%)']

# Display the aggregated data grid to verify layout before plotting the bar chart
chart1_data

import matplotlib.pyplot as plt

# Set the figure size for clear rendering of the bar chart
plt.figure(figsize=(8, 5))

# Generate vertical bar chart using the aggregated payment methods dataset
bars = plt.bar(chart1_data['Payment Method'], chart1_data['Return Rate (%)'], color=['red', 'orange', 'blue'], edgecolor='black')

# Label plot coordinates and add descriptive analytical title text
plt.xlabel('Payment Method')
plt.ylabel('Return Rate (%)')
plt.title('Return Rate by Payment Method (COD Returns at 44.4%)')
plt.ylim(0, 50)

# Loop through each individual bar layer to explicitly write numerical percentages on top
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval}%", ha='center', va='bottom', fontweight='bold')

# Ensure visualization path directory exists locally before writing file frame
import os
os.makedirs('visualizations', exist_ok=True)

# Save the final rendered graph framework cleanly as a localized PNG image target
plt.savefig('visualizations/return_rate_by_payment.png', bbox_inches='tight')

# Display the final rendered static plot explicitly on the Colab execution canvas
plt.show()

# Set the figure size for clear rendering of the line trend chart
plt.figure(figsize=(8, 5))

# Generate line plot using the monthly trend data without outliers from Task 10
plt.plot(series_exc['Year-Month'], series_exc['Total (Without Outliers)'], marker='o', color='purple', linewidth=2, linestyle='-')

# Label plot coordinates and add descriptive title highlighting March as the genuine peak
plt.xlabel('Year-Month')
plt.ylabel('Total Revenue (INR)')
plt.title('Monthly Revenue Trend - Outlier-Corrected (March is Genuine Peak)')
plt.grid(True, linestyle='--', alpha=0.6)

# Save the final rendered graph framework cleanly as a localized PNG image target
plt.savefig('visualizations/monthly_revenue_trend.png', bbox_inches='tight')

# Display the final rendered static plot explicitly on the Colab execution canvas
plt.show()
