import json
import csv

try:
    with (open("suppliers.csv", "r", encoding="utf-8") as r_csvfile,
          open("orders.json", "r", encoding="utf-8") as r_jsonfile,
          open("supplier_costs.csv", "w", encoding="utf-8", newline="") as w_csvfile):
        read_data = json.load(r_jsonfile)
        reader = csv.DictReader(r_csvfile)
        suppliers = list(reader)
        if read_data and suppliers:
            orders = {}
            for product in read_data:
                orders[product['supplier_id']] = orders.get(product['supplier_id'], 0) + int(product['price']) * float(
                    product['quantity'])
            supplier_costs = [
                {'supplier_id': supplier['supplier_id'], 'name': supplier['name'], 'region': supplier['region'],
                 'total_cost': orders[supplier['supplier_id']]} for supplier in suppliers if
                supplier['supplier_id'] in orders]
            writer = csv.DictWriter(w_csvfile, fieldnames=['supplier_id', 'name', 'region', 'total_cost'])
            writer.writeheader()
            writer.writerows(supplier_costs)
            print("File supplier_costs.csv created successfully")
        else:
            print("No data found in suppliers.csv or orders.json")
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("JSON decode error")
except KeyError:
    print("Missing 'supplier_id' or 'price' or 'quantity' keys ")
except ValueError:
    print("Invalid 'price' or 'quantity' value")
except Exception as e:
    print(f"Error: {e}")
