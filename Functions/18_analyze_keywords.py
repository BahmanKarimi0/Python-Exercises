import re
from typing import Union


def analyze_keywords(filename: str, min_length: int, min_count: int) -> Union[dict[str, int], dict[str, str]]:
    try:
        words_count: dict[str, int] = {}
        with open(filename, 'r', encoding='utf-8') as f:

            for line in f:
                words = re.findall(r'\w+', line.casefold())
                for word in words:
                    if len(word) >= min_length:
                        words_count[word.casefold()] = words_count.get(word.casefold(), 0) + 1

        keywords: dict[str, int] = {}
        for word, count in words_count.items():
            if count >= min_count:
                keywords[word] = count
        final_keywords: dict[str, int] = {}
        for word, count in keywords.items():
            is_substring = False
            for other_word in keywords:
                if word != other_word and word in other_word:
                    is_substring = True
                    break
            if not is_substring:
                final_keywords[word] = count
        return final_keywords
    except FileNotFoundError:
        return {"Error": "File not found"}
    except Exception as e:
        return {"Error": str(e)}


print(analyze_keywords("logs.txt", 4, 2))
