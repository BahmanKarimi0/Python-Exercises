import json
import csv

try:
    with open('orders.json', 'r', encoding="utf-8") as jsonfile, open('customers.csv', 'r',
                                                                      encoding='utf-8') as rcsvfile, open(
        'customer_totals.csv', 'w', encoding="utf-8", newline='') as wcsvfile:
        read_data = json.load(jsonfile)
        reader = csv.DictReader(rcsvfile)
        customers = list(reader)
        customer_orders = {}
        if read_data and customers:
            for order in read_data:
                order['customer_id'] = int(order['customer_id'])
                order['amount'] = float(order['amount'])
                customer_orders[order['customer_id']] = customer_orders.get(order['customer_id'], 0) + order['amount']
            total_orders = [{'customer_id': int(customer['customer_id']), 'name': customer['name'],
                             'total_amount': customer_orders[int(customer['customer_id'])]} for customer in customers if
                            int(customer['customer_id']) in customer_orders]

            writer = csv.DictWriter(wcsvfile, fieldnames=['customer_id', 'name', 'total_amount'])
            writer.writeheader()
            writer.writerows(total_orders)
            print("File customer_totals.csv created successfully")
        else:
            print("No data available in 'orders.json' or 'customers.csv'")
except FileNotFoundError:
    print("File not found")
except KeyError:
    print("Missing 'customer_id' or 'amount' or 'name'")
except json.JSONDecodeError:
    print("Json decode error")
except ValueError:
    print("Invalid 'customer_id' or 'amount' or 'name' value")
except PermissionError :
    print("Permission denied")
except Exception as e:
    print(f"Error: {e}")