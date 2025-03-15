import csv
import json

try:
    with (open("sales.csv", "r", encoding="utf-8") as rf,
          open("total_sales.json", "w", encoding="utf-8") as wf):
        reader = csv.DictReader(rf)
        products = list(reader)
        if products:
            total_sales = {}
            for product in products:
                total_sales[product['product']] = total_sales.get(product['product'], 0) + int(product['quantity'])
            json.dump(total_sales, wf, indent=4)
            print("File total_sales.json created successfully")
        else:
            print("No products found in sales.csv")
except FileNotFoundError:
    print("File sales.csv not found")
except PermissionError:
    print("Permission denied")
except KeyError:
    print("Missing 'product' or 'quantity' key")
except ValueError:
    print("Invalid 'quantity' value")
except Exception as e:
    print(f"Error: {e}")
