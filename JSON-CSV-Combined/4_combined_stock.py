import csv
import json

try:
    with open("inventory.csv", "r", encoding="utf-8") as csvfile, open("sales.json", "r",
                                                                       encoding="utf-8") as rjsonfile, open(
            "remaining_stock.json", "w", encoding="utf-8") as wjsonfile:
        read_data = json.load(rjsonfile)
        reader = csv.DictReader(csvfile)
        stocks = list(reader)

        total_sales = {}
        if read_data and stocks:
            for product in read_data:
                product['quantity'] = int(product['quantity'])
                total_sales[product['product']] = total_sales.get(product['product'], 0) + product['quantity']

            remaining_stock = {}
            for stock in stocks:
                stock['stock'] = int(stock['stock'])
                if stock['product'] in total_sales:
                    remaining_stock[stock['product']] = stock['stock'] - total_sales[stock['product']]

            json.dump(remaining_stock, wjsonfile, indent=4)
            print("File remaining_stock.json created successfully")
        else:
            print("No data available in sales.json or in inventory.csv")

except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Json decode error")
except PermissionError:
    print("Permission denied")
except KeyError:
    print("Missing 'quantity' or 'product' or 'stock' key")
except ValueError:
    print("Invalid 'quantity' or 'stock' value")
except Exception as e:
    print(f"Error: {e}")
