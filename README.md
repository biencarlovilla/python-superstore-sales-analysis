
# Python Superstore Sales Analysis

## Project Overview
This project analyzes retail sales data using Python to identify sales trends, profitability, and regional performance.

The analysis uses the Sample Superstore dataset containing 9,994 records.

## Tools Used
- Python
- Pandas
- Matplotlib
- PyCharm

## Project Process
1. Imported the Superstore CSV dataset.
2. Inspected the dataset for missing values and duplicates.
3. Converted date columns into datetime format.
4. Calculated total sales, profit, and orders.
5. Analyzed sales and profit by product category.
6. Compared sales and profit across regions.
7. Created charts to visualize business performance.

## Key Findings
- Total Sales: $2,297,200.86
- Total Profit: $286,397.02
- Total Orders: 5,009
- Technology generated the highest sales and profit.
- Furniture generated high sales but relatively low profit.
- The West region generated the highest sales and profit.

## Visualizations
- Total Sales by Category
- Total Profit by Category
- Total Sales by Region
- Monthly Sales Trend

## Project Files
- `main.py` - Python analysis code
- `data/` - Original dataset
- `images/` - Analysis screenshots and charts
- `pyproject.toml` - Project dependencies
- `uv.lock` - Dependency lockfile

## How to Run
1. Clone or download this repository.
2. Install dependencies using `uv sync`.
3. Run the analysis using `uv run python main.py`.
