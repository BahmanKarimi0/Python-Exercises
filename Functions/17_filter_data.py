from typing import Union


def filter_data(filename: str, keyword: str) -> Union[list[str], dict[str, str]]:
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            filtered_data = [line for line in f if keyword.casefold() in line.casefold()]
        return filtered_data
    except FileNotFoundError:
        return {"Error": "File Not Found"}
    except Exception as e:
        return {"Error": f"{e}"}


print(filter_data("data.txt", "temperature"))
