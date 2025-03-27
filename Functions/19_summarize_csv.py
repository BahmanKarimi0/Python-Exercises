import csv
from typing import Union


def summarize_csv(filename: str, column_name: str) -> Union[dict[str, Union[int, float]], dict[str, str]]:
    try:
        summarize: dict[str, Union[int, float]] = {"sum": 0, "count": 0}
        with open(filename, 'r', encoding="utf-8") as f:
            sales = csv.DictReader(f)
            sum_sales: float = 0
            count: int = 0
            for sale in sales:
                try:
                    sum_sales += float(sale[column_name])
                    count += 1
                except:
                    continue
            if sum_sales.is_integer():
                sum_sales = int(sum_sales)

            summarize["sum"] = sum_sales
            summarize["count"] = count
        return summarize
    except FileNotFoundError:
        return {"ERROR": "File not found"}
    except KeyError:
        return {"ERROR": f"Missing {column_name} key"}
    except Exception as e:
        return {"ERROR": str(e)}


print(summarize_csv("sales.csv", "quantity"))
