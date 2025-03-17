import json
import csv

try:
    with (open("sales.json", "r", encoding="utf-8") as r_jsonfile,
          open("products.csv", "r", encoding="utf-8") as r_csvfile,
          open("march_revenue.json", "w", encoding="utf-8") as w_jsonfile):
        read_data = json.load(r_jsonfile)
        reader = csv.DictReader(r_csvfile)
        products = list(reader)
        total_sales = {}
        if read_data and products:
            for sales in read_data:
                if "2025-03" in sales["date"]:
                    total_sales[sales['product_id']] = total_sales.get(sales['product_id'], 0) + int(sales['quantity'])
            if total_sales:
                march_revenue = {}
                for product in products:
                    if product['product_id'] in total_sales:
                        march_revenue[product['product_id']] = float(
                            product['price']) * total_sales[product['product_id']]
                json.dump(march_revenue, w_jsonfile, indent=4)
                print("File march_revenue.json created successfully")
            else:
                print("No sales found in March 2025")
        else:
            print("No data available in sales.json or products.csv")
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("JSON decode error")
except PermissionError:
    print("Permission denied")
except KeyError:
    print("Missing 'product_id' or 'price' or 'quantity' or 'date' key")
except ValueError:
    print("Invalid 'product_id' or 'price' or 'quantity' or 'date' value")

except Exception as e:
    print(f"Error: {e}")
