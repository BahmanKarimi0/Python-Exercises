import json
import csv


def calculate_region_product_profit(json_filename, csv_filename, output_filename):
    try:
        with (open(json_filename, "r", encoding="utf-8") as r_jsonfile,
              open(csv_filename, "r", encoding="utf-8") as r_csvfile):
            orders = json.load(r_jsonfile)
            products = list(csv.DictReader(r_csvfile))

            all_region = {order['region'] for order in orders}
            if orders and products:
                product_sells = {}
                for order in orders:
                    product_id = order["product_id"]
                    amount = order["amount"]
                    region = order["region"]
                    product_sells[product_id] = product_sells.get(product_id, {})
                    product_sells[product_id][region] = product_sells[product_id].get(region, 0) + float(amount)

                region_product_profit = []
                for product in products:
                    product_id = product["product_id"]
                    all_products = product_sells.get(product_id, {})
                    for region in all_region:
                        profit = all_products.get(region, 0)
                        if profit:
                            total_profit = profit - float(product['unit_cost'])
                        else:
                            total_profit = 0
                        region_product_profit.append(
                            {'region': region, 'product_id': product_id, 'name': product['name'], 'total_profit': total_profit})

                with open(output_filename, "w", encoding="utf-8", newline="") as output_file:
                    writer = csv.DictWriter(output_file, fieldnames=['region', 'product_id', 'name', 'total_profit'])
                    writer.writeheader()
                    writer.writerows(region_product_profit)
                    return {"Success": f"{output_filename} has been created successfully."}
            else:
                return {"Error": f"No data found in {json_filename} or {csv_filename}."}
    except FileNotFoundError:
        return {"Error": "File not found"}
    except PermissionError:
        return {"Error": "Permission denied"}
    except json.JSONDecodeError:
        return {"Error": "Invalid JSON decode"}
    except KeyError:
        return {"Error": "Missing 'product_id' or 'amount' or 'region' or 'unit_cost' key"}
    except ValueError:
        return {"Error": "Invalid 'amount' or 'unit_cost' value"}
    except Exception as e:
        return {"Error": str(e)}



print(calculate_region_product_profit("orders.json", "products.csv", "region_product_profit.csv"))

