import csv
import json

try:
    with (open("sales.json", "r", encoding="utf-8") as rf,
          open("revenue.csv", "w", encoding="utf-8", newline="") as wf):
        read_data = json.load(rf)
        revenue = {}
        if read_data:
            for product in read_data:
                revenue[product['product']] = revenue.get(product['product'], 0) + int(product['quantity']) * int(
                    product['price'])
            revenue_dict = [{'product': name, 'revenue': value} for name, value in revenue.items()]
            writer = csv.DictWriter(wf, fieldnames=revenue_dict[0].keys())
            writer.writeheader()
            writer.writerows(revenue_dict)
            print("File revenue.csv created successfully")
        else:
            print("No products found in sales.json")
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("JSON decode error")
except KeyError:
    print("Missing 'product', 'quantity', or 'price' key")
except ValueError:
    print("Invalid 'quantity' or 'price' value")
except Exception as e:
    print(f"Error: {e}")
