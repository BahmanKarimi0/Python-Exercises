import json
import csv

try:
    with open("sales.json", "r", encoding="utf-8") as r_jsonfile, open("products.csv", "r",
                                                                       encoding="utf-8") as r_csvfile:
        sales = json.load(r_jsonfile)
        products = list(csv.DictReader(r_csvfile))
        if sales and products:
            all_regions = {region['region'] for region in sales}
            region_sales = {}
            for sale in sales:
                product_id = sale['product_id']
                region = sale['region']
                total_costs = int(sale['quantity']) * float(sale['price'])
                region_sales[product_id] = region_sales.get(product_id, {})
                region_sales[product_id][region] = region_sales[product_id].get(region, 0) + total_costs

            category_data = {
                product['category']: {'total_regional_sales': 0, 'active_region': set(), 'best_seller_count': 0} for
                product
                in products}

            product_sales = []
            for product in products:
                product_id = product['product_id']
                regions = region_sales.get(product_id, {})
                active_region = len(regions)

                sum_of_regional_sales = sum(regions.values())
                is_best_seller = "yes" if sum_of_regional_sales > 10000 and active_region >= 3 else "no"
                category = product['category']
                category_data[category]['total_regional_sales'] += sum_of_regional_sales
                category_data[category]['active_region'].update(regions.keys())

                if is_best_seller == "yes":
                    category_data[category]['best_seller_count'] += 1
                for region in all_regions:
                    total_region = regions.get(region, 0)
                    product_sales.append(
                        {'product_id': product_id, 'name': product['name'], 'category': product['category'],
                         'region': region,
                         'total_sales': total_region, 'is_best_seller': is_best_seller})
            with open("product_sales.csv", "w", encoding="utf-8", newline="") as w_csvfile:
                writer = csv.DictWriter(w_csvfile,
                                        fieldnames=['product_id', 'name', 'category', 'region', 'total_sales',
                                                    'is_best_seller'])
                writer.writeheader()
                writer.writerows(product_sales)
            category_summary = []
            print(category_data)
            for category, data in category_data.items():
                # print(data['active_region'])
                print(data['total_regional_sales'])
                active_region_count = len(data['active_region']) or 1

                avg_regional_sales = round(data['total_regional_sales'] / active_region_count, 2)
                category_summary.append({
                    'category': category,
                    'avg_regional_sales': avg_regional_sales,
                    'best_seller_count': data['best_seller_count']
                })
            with open("category_summary.csv", "w", encoding="utf-8", newline="") as w_csvfile:
                writer = csv.DictWriter(w_csvfile,
                                        fieldnames=['category', 'avg_regional_sales', 'best_seller_count'])
                writer.writeheader()
                writer.writerows(category_summary)
            print("Files product_sales.csv and category_summary.csv created successfully")
        else:
            print("No data found in 'sales.json' or 'products.csv'")
except FileNotFoundError:
    print("File 'sales.json' or 'products.csv' not found")
except PermissionError:
    print("Permission denied")
except json.decoder.JSONDecodeError:
    print("JSON decode error")
except KeyError:
    print("Missing 'region' or 'category' or 'quantity' or 'price' or 'product_id' key ")
except ValueError:
    print("Invalid 'quantity' or 'price' value")
except Exception as e:
    print(f"Error: {e}")
