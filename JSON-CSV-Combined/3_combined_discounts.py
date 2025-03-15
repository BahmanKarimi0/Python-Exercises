import csv
import json

try:
    with open("sales.csv", "r", encoding="utf-8") as csv_f, open("discounts.json", "r",
                                                                 encoding="utf-8") as json_f, open(
            "discounted_prices.csv", "w", encoding="utf-8", newline="") as csv_discount_f:
        read_data = json.load(json_f)
        reader = csv.DictReader(csv_f)
        products = list(reader)
        discount_price = {}
        if products:
            for product in products:
                product['price'] = float(product['price'])
                if product['product'] in read_data:
                    discount_price[product['product']] = float(product['price']) * (1 - read_data[product['product']])
            writer = csv.DictWriter(csv_discount_f, ['product', 'discounted_price'])
            writer.writeheader()
            writer.writerows(
                [{'product': product, 'discounted_price': discount} for product, discount in discount_price.items()])
            print("File discounted_prices.csv created successfully")
        else:
            print("No products found in sales.csv")
except FileNotFoundError:
    print("File not found")
except json.decoder.JSONDecodeError:
    print("Json decode error")
except ValueError:
    print("Invalid 'quantity' or 'price' value")
except KeyError:
    print("Missing 'product' or 'price' or 'quantity' key")
except Exception as e:
    print(f"Error: {e}")
