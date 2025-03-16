# JSON and CSV Combined Exercises
This directory contains 15 Python exercises combining JSON and CSV file handling, designed for practical data science applications. The exercises are split into three levels: Basic (1-5), Intermediate (6-10), and Challenging (11-15). Each exercise processes data between `sales.csv` (with "product", "quantity", "price" columns) and JSON files.

## Objectives
- Combine CSV and JSON data processing.
- Perform data aggregation, filtering, and transformation.
- Prepare data for analysis in data science workflows.

## Exercises
Below are the 15 exercises with their descriptions and solutions.

### Exercise 1: Calculate Total Sales from CSV to JSON
**Question:**  
Write a Python program that reads `sales.csv` (with columns "product", "quantity", "price"), calculates the total quantity sold per product, and saves the result to `total_sales.json` as a dictionary. Handle errors like missing files or invalid data.

**Solution:** See `1_csv_to_json_sales.py`.

=================================================================

### Exercise 2: Calculate Revenue from JSON to CSV
**Question:**  
Write a Python program that reads `sales.json` (a list of dictionaries with "product", "quantity", "price"), calculates the total revenue (quantity × price) per product, and saves the result to `revenue.csv` with columns "product" and "revenue". Handle errors like missing files or invalid data.

**Solution:** See `2_json_to_csv_revenue.py`.

=================================================================

### Exercise 3: Calculate Discounted Prices from CSV and JSON
**Question:**  
Write a Python program that reads `sales.csv` (with columns "product", "quantity", "price") and `discounts.json` (a dictionary of product names and discount percentages), calculates the discounted price (price × (1 - discount)) for products present in both files, and saves the result to `discounted_prices.csv` with columns "product" and "discounted_price". Handle errors like missing files or invalid data.

**Solution:** See `3_combined_discounts.py`.

=================================================================

### Exercise 4: Calculate Remaining Stock from CSV and JSON
**Question:**  
Write a Python program that reads `inventory.csv` (with columns "product", "stock") and `sales.json` (a list of dictionaries with "product", "quantity", "price"), calculates the remaining stock (stock - total quantity) for products present in both files, and saves the result to `remaining_stock.json` as a dictionary. Handle errors like missing files or invalid data.

**Solution:** See `4_combined_stock.py`.

==================================================================
