import re
from typing import Union


def count_words(filename: str) -> dict[str, Union[int, str]]:
    try:
        word_counts = {}
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                words = re.findall(r"\w+", line.casefold())
                for word in words:
                    word_counts[word] = word_counts.get(word, 0) + 1
        return word_counts
    except FileNotFoundError:
        return {"ERROR": "File not found"}
    except Exception as e:
        return {"ERROR": f"Error: {e}"}


print(count_words("sample.txt"))
