
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
try:
    revenue_df = pd.read_csv('nu_revenue.csv', index_col=0, parse_dates=True)
except FileNotFoundError:
    print("Error: nu_revenue.csv not found. Please run the get_data.py script first.")
    exit()

# --- Data Cleaning ---
# Drop rows with missing values
revenue_df.dropna(inplace=True)

# Ensure the data is numeric
revenue_df['Revenue'] = pd.to_numeric(revenue_df['Revenue'])

# --- Exploratory Data Analysis (EDA) ---
if not revenue_df.empty:
    print("Nubank Quarterly Revenue (in billions USD):")
    print(revenue_df / 1e9) # Display revenue in billions for readability

    # Plotting the data
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 6))

    sns.lineplot(x=revenue_df.index, y=revenue_df['Revenue'], marker='o', linestyle='-')

    plt.title('Nubank Quarterly Revenue', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Revenue (in billions USD)', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot
    plt.savefig('nu_revenue_plot.png')
    print("\nRevenue plot saved as nu_revenue_plot.png")
else:
    print("No data available to plot after cleaning.")

