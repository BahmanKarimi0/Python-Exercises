import json
import csv

try:
    with (open("inventory.json", "r", encoding="utf-8") as r_jsonfile,
          open("stores.csv", "r",encoding="utf-8") as r_csvfile,
          open("store_inventory.csv", "w", encoding="utf-8", newline="") as w_csvfile):
        read_data = json.load(r_jsonfile)
        reader = csv.DictReader(r_csvfile)
        stores = list(reader)
        if read_data and stores:
            inventory_data = {}
            for product in read_data:
                inventory_data[product["store_id"]] = inventory_data.get(product["store_id"], {})
                inventory_data[product["store_id"]][product['product']] = inventory_data[product['store_id']].get(
                    product['product'], 0) + int(product['quantity'])
            store_inventory = []
            for store in stores:
                if store['store_id'] in inventory_data:
                    for product, value in inventory_data[store["store_id"]].items():
                        store_inventory.append(
                            {'store_id': store['store_id'], 'location': store['location'], 'product': product,
                             'total_quantity': value})
            writer = csv.DictWriter(w_csvfile, fieldnames=['store_id', 'location', 'product', 'total_quantity'])
            writer.writeheader()
            writer.writerows(store_inventory)
            print("File store_inventory.csv created successfully")
        else:
            print("No stores.csv or inventory.json found")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except json.JSONDecodeError:
    print("JSON decode error")
except KeyError:
    print("Missing 'store_id' or 'product' or 'quantity' key")
except ValueError:
    print("Invalid 'quantity' value ")
except Exception as e:
    print(f"Error: {e}")
