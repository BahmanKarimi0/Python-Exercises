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

### Exercise 5: Calculate Customer Order Totals from CSV and JSON
**Question:**  
Write a Python program that reads `customers.csv` (with columns "customer_id", "name") and `orders.json` (a list of dictionaries with "order_id", "customer_id", "amount"), calculates the total order amount per customer for those present in both files, and saves the result to `customer_totals.csv` with columns "customer_id", "name", and "total_amount". Handle errors like missing files or invalid data.

**Solution:** See `5_combined_customer_totals.py`.

================================================================

### Exercise 6: Calculate March 2025 Revenue from CSV and JSON
**Question:**  
Write a Python program that reads `products.csv` (with columns "product_id", "name", "price") and `sales.json` (a list of dictionaries with "sale_id", "product_id", "quantity", "date"), calculates the total revenue (price × quantity) per product for sales in March 2025 only, and saves the result to `march_revenue.json` as a dictionary for products present in both files. Handle errors like missing files or invalid data.

**Solution:** See `6_march_revenue.py`.

===============================================================

### Exercise 7: Calculate Completed Task Hours from CSV and JSON
**Question:**  
Write a Python program that reads `employees.csv` (with columns "employee_id", "name", "department") and `tasks.json` (a list of dictionaries with "task_id", "employee_id", "hours", "status"), calculates the total hours per employee for tasks with "completed" status, and saves the result to `completed_hours.csv` with columns "employee_id", "name", "department", and "total_hours" for employees present in both files. Set total_hours to 0 for employees with no completed tasks. Handle errors like missing files or invalid data.

**Solution:** See `7_completed_hours.py`.

==============================================================

### Exercise 8: Calculate Store Inventory Totals from CSV and JSON
**Question:**  
Write a Python program that reads `stores.csv` (with columns "store_id", "location") and `inventory.json` (a list of dictionaries with "inventory_id", "store_id", "product", "quantity"), calculates the total quantity per product per store, and saves the result to `store_inventory.csv` with columns "store_id", "location", "product", and "total_quantity" for stores present in both files. Aggregate quantities if a product appears multiple times in a store. Handle errors like missing files or invalid data.

**Solution:** See `8_store_inventory.py`.

============================================================

### Exercise 9: Calculate Supplier Costs from CSV and JSON
**Question:**  
Write a Python program that reads `suppliers.csv` (with columns "supplier_id", "name", "region") and `orders.json` (a list of dictionaries with "order_id", "supplier_id", "product", "quantity", "price"), calculates the total cost (quantity × price) per supplier, and saves the result to `supplier_costs.csv` with columns "supplier_id", "name", "region", and "total_cost" for suppliers present in both files. Handle errors like missing files or invalid data.

**Solution:** See `9_supplier_costs.py`.

============================================================

### Exercise 10: Calculate Customer Spending in 2025 from CSV and JSON
**Question:**  
Write a Python program that reads `customers.csv` (with columns "customer_id", "name", "city") and `purchases.json` (a list of dictionaries with "purchase_id", "customer_id", "product", "amount", "date"), calculates the total spending (amount) per customer for purchases in 2025 only, and saves the result to `customer_spending_2025.csv` with columns "customer_id", "name", "city", and "total_spending" for customers present in both files. Set total_spending to 0 for customers with no 2025 purchases. Handle errors like missing files or invalid data.

**Solution:** See `10_customer_spending_2025.py`.

===========================================================

### Exercise 11: Project Expense Summary from CSV and JSON
**Question:**  
Write a Python program that reads `projects.csv` (with columns "project_id", "name", "budget") and `expenses.json` (a list of dictionaries with "expense_id", "project_id", "category", "amount", "date"), calculates total expenses per category per project and their percentage of the budget, and saves the result to `project_expense_summary.csv` with columns "project_id", "name", "budget", "category", "total_amount", and "percentage" for projects present in both files. Include all categories with 0 for projects with no expenses. Handle errors.

**Solution:** See `11_project_expense_summary.py`.

==========================================================

### Exercise 12: Employee Work Summary from CSV and JSON
**Question:**  
Write a Python program that reads `employees.csv` (with columns "employee_id", "name", "department") and `timesheets.json` (a list of dictionaries with "timesheet_id", "employee_id", "date", "hours_worked"), calculates total hours worked per month and monthly average for each employee in 2025, and saves the result to `employee_work_summary.csv` with columns "employee_id", "name", "department", "month", "total_hours", and "monthly_average" for employees present in both files. Set total_hours to 0 for months with no work, excluding them from the average. Handle errors.

**Solution:** See `12_employee_work_summary.py`.

=========================================================

### Exercise 13: Inventory Summary from CSV and JSON
**Question:**  
Write a Python program that reads `inventory.csv` (with columns "item_id", "name", "category", "stock") and `transactions.json` (a list of dictionaries with "transaction_id", "item_id", "type" ["sale" or "restock"], "quantity", "date"), updates current stock based on transactions (subtract sales, add restocks), calculates total sold and restocked per item in 2025, and saves the result to `inventory_summary.csv` with columns "item_id", "name", "category", "initial_stock", "current_stock", "total_sold", "total_restocked" for items present in both files. Ignore transactions outside 2025. Handle errors.

**Solution:** See `13_inventory_summary.py`.

========================================================

### Exercise 14: Customer Orders and Region Summary from CSV and JSON
**Question:**  
Write a Python program that reads `customers.csv` (columns: "customer_id", "name", "region") and `orders.json` (list of dictionaries with "order_id", "customer_id", "date", "items" [list of {"item_id", "quantity", "price"}]), calculates total cost per customer per month in 2025, identifies VIP customers (orders in ≥3 months and total cost > 5000), computes average monthly cost and VIP count per region, and saves results to `customer_orders.csv` ("customer_id", "name", "region", "month", "total_cost", "is_vip") and `region_summary.csv` ("region", "avg_monthly_cost", "vip_count"). Ignore non-2025 orders. Handle errors.

**Solution:** See `14_customer_orders.py`.  
**Data:** See `customers.csv` (45 customers) and `orders.json` (75 orders).

=======================================================

