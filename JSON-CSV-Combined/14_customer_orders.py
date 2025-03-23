import json
import csv

try:
    with (open("orders.json", "r", encoding="utf-8") as r_jsonfile,
          open("customers.csv", "r", encoding="utf-8") as r_csvfile):
        orders = json.load(r_jsonfile)
        readers = csv.DictReader(r_csvfile)
        customers = list(readers)
        if orders and customers:
            all_2025_months = [f"2025-{i:02d}" for i in range(1, 13)]  # همه ۱۲ ماه
            items_orders = {}
            for order in orders:
                if "2025" in order["date"]:
                    customer_id = order["customer_id"]
                    order_month = order["date"][:7]
                    items_orders[customer_id] = items_orders.get(customer_id, {})
                    for item in order["items"]:
                        items_orders[customer_id][order_month] = items_orders[customer_id].get(order_month, 0) + \
                            int(item["quantity"]) * float(item["price"])

            region_data = {customer["region"]: {"total_cost": 0, "active_months": set(), "vip_count": 0}
                          for customer in customers}
            customer_orders = []
            for customer in customers:
                customer_id = customer["customer_id"]
                costs = items_orders.get(customer_id, {})
                active_order_month = len(costs)
                sum_of_orders = sum(costs.values())
                is_vip = "yes" if sum_of_orders >= 5000 and active_order_month >= 3 else "no"
                if costs:
                    region = customer["region"]
                    region_data[region]["total_cost"] += sum_of_orders
                    region_data[region]["active_months"].update(costs.keys())
                    if is_vip == "yes":
                        region_data[region]["vip_count"] += 1
                for month in all_2025_months:
                    total_cost = costs.get(month, 0)
                    customer_orders.append({
                        "customer_id": customer_id,
                        "name": customer["name"],
                        "region": customer["region"],
                        "month": month,
                        "total_cost": total_cost,
                        "is_vip": is_vip
                    })

            with open("customer_orders.csv", "w", encoding="utf-8", newline="") as w_csvfile:
                writer = csv.DictWriter(w_csvfile, fieldnames=["customer_id", "name", "region", "month", "total_cost", "is_vip"])
                writer.writeheader()
                writer.writerows(customer_orders)

            region_summary = []
            for region, data in region_data.items():
                active_months_count = len(data["active_months"]) or 1
                avg_cost = round(data["total_cost"] / active_months_count, 2)
                region_summary.append({"region": region, "avg_monthly_cost": avg_cost, "vip_count": data["vip_count"]})

            with open("region_summary.csv", "w", encoding="utf-8", newline="") as w_regfile:
                reg_writer = csv.DictWriter(w_regfile, fieldnames=["region", "avg_monthly_cost", "vip_count"])
                reg_writer.writeheader()
                reg_writer.writerows(region_summary)

            print("Files customer_orders.csv and region_summary.csv created successfully")
        else:
            print("No data available in customers.csv and orders.json")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except json.JSONDecodeError:
    print("JSON decode error")
except KeyError:
    print("Missing 'customer_id' or 'date' or 'item_id' or 'quantity' or 'price'")
except ValueError:
    print("Invalid 'quantity' or 'price' value")
except Exception as e:
    print(f"Error: {e}")