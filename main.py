
import pandas as pd
import matplotlib.pyplot as plt

# Load the Superstore dataset
df = pd.read_csv("data/Sample - Superstore.csv", encoding="cp1252")

# Display the first five rows
print("Superstore Dataset Preview:")
print(df.head())

# Check dataset size
print("\nDataset Size:")
print(df.shape)

# Check column names
print("\nColumn Names:")
print(df.columns.tolist())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check for duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y")

# Verify date formats
print("\nUpdated Date Types:")
print(df[["Order Date", "Ship Date"]].dtypes)

# Calculate key sales metrics
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()

# Display sales summary
print("\nSales Performance Summary:")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders:,}")

# Calculate total sales by category
category_sales = df.groupby("Category")["Sales"].sum()

# Sort categories by highest sales
category_sales = category_sales.sort_values(ascending=False)

# Display results
print("\nSales by Category:")
print(category_sales.round(2))

# Calculate total profit by category
category_profit = df.groupby("Category")["Profit"].sum()

# Sort categories by highest profit
category_profit = category_profit.sort_values(ascending=False)

# Display results
print("\nProfit by Category:")
print(category_profit.round(2))

# Calculate total sales by region
regional_sales = df.groupby("Region")["Sales"].sum()

# Sort regions by highest sales
regional_sales = regional_sales.sort_values(ascending=False)

# Display results
print("\nSales by Region:")
print(regional_sales.round(2))

# Calculate total profit by region
regional_profit = df.groupby("Region")["Profit"].sum()

# Sort regions by highest profit
regional_profit = regional_profit.sort_values(ascending=False)

# Display results
print("\nProfit by Region:")
print(regional_profit.round(2))

# Create sales by category chart
category_sales.plot(kind="bar")

# Add chart labels
plt.title("Total Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales ($)")

# Improve layout
plt.xticks(rotation=0)
plt.tight_layout()

# Display chart
plt.show()

# Create profit by category chart
category_profit.plot(kind="bar")

# Add chart labels
plt.title("Total Profit by Category")
plt.xlabel("Product Category")
plt.ylabel("Total Profit ($)")

# Improve layout
plt.xticks(rotation=0)
plt.tight_layout()

# Display chart
plt.show()

# Create regional sales chart
regional_sales.plot(kind="bar")

# Add chart labels
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales ($)")

# Improve layout
plt.xticks(rotation=0)
plt.tight_layout()

# Display chart
plt.show()


# Calculate monthly sales
monthly_sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Sales"].sum()

# Create monthly sales trend chart
monthly_sales.index = monthly_sales.index.to_timestamp()
monthly_sales.plot(kind="line", marker="o", figsize=(12, 5))

# Add chart labels
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")

# Improve layout
plt.grid(True)
plt.tight_layout()

# Display chart
plt.show()
