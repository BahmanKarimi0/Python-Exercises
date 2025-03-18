import json
import csv

try:
    with (open("purchases.json", "r", encoding="utf-8") as r_jsonfile,
          open("customers.csv", "r", encoding="utf-8") as r_csvfile,
          open("customer_spending_2025.csv", "w", encoding="utf-8", newline="") as w_csvfile):
        read_data = json.load(r_jsonfile)
        reader = csv.DictReader(r_csvfile)
        customers = list(reader)
        if read_data and customers:
            items = {}
            for item in read_data:
                if "2025" in item['date']:
                    items[item['customer_id']] = items.get(item['customer_id'], 0) + float(item['amount'])

            customer_spending_2025 = []
            for customer in customers:
                total_spending = items.get(customer['customer_id'], 0)
                customer_spending_2025.append(
                    {'customer_id': customer['customer_id'], 'name': customer['name'], 'city': customer['city'],
                     'total_spending': total_spending})
            writer = csv.DictWriter(w_csvfile, fieldnames=['customer_id', 'name', 'city', 'total_spending'])
            writer.writeheader()
            writer.writerows(customer_spending_2025)
            print("File customer_spending_2025.csv created successfully")
        else:
            print("No data found in customers.csv or purchases.json")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except json.JSONDecodeError:
    print("JSON decode error")
except KeyError:
    print("Missing 'customer_id' or 'amount' or 'date' key ")
except ValueError:
    print("Invalid 'amount' value")
except Exception as e:
    print(f"Error: {e}")
