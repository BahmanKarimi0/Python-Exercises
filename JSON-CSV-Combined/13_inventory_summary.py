import json
import csv

try:
    with (open("transactions.json", "r", encoding="utf-8") as r_jsonfile,
          open("inventory.csv", "r", encoding="utf-8") as r_csvfile,
          open("inventory_summary.csv", "w", encoding="utf-8", newline="") as w_jsonfile):
        transactions = json.load(r_jsonfile)
        reader = csv.DictReader(r_csvfile)
        inventories = list(reader)
        if transactions and inventories:
            transactions_type = {}
            for transaction in transactions:
                if "2025" in transaction["date"]:
                    item_id = transaction["item_id"]
                    types = transaction["type"]
                    transactions_type[item_id] = transactions_type.get(item_id, {})
                    transactions_type[item_id][types] = transactions_type[item_id].get(types, 0) + int(
                        transaction["quantity"])
            inventory_summary = []
            for inventory in inventories:
                item_id = inventory["item_id"]
                trans_by_item = transactions_type.get(item_id, {})
                total_sold = trans_by_item.get('sale', 0)
                total_restock = trans_by_item.get('restock', 0)
                current_stock = int(inventory['stock']) - total_sold + total_restock

                inventory_summary.append(
                    {'item_id': item_id, 'name': inventory['name'], 'category': inventory['category'],
                     'initial_stock': inventory['stock'], 'current_stock': current_stock,
                     'total_sold': total_sold, 'total_restocked': total_restock})
            writer = csv.DictWriter(w_jsonfile, fieldnames=inventory_summary[0].keys())
            writer.writeheader()
            writer.writerows(inventory_summary)
            print("File inventory_summary.csv created successfully")
        else:
            print("No data found in 'transactions.json' or 'inventory.csv'")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except json.JSONDecodeError:
    print("JSON decode error")
except KeyError:
    print("Missing required key in data")
except ValueError:
    print("Invalid 'quantity' or 'stock' value")
except Exception as e:
    print(f"Error: {e}")
