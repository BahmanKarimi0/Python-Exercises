def file_lines(filename, keyword):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if keyword.casefold() in line.casefold():
                    yield line
    except FileNotFoundError:
        yield 'File not found'


for line in file_lines("data.txt", "test"):
    print(line.strip())
for line in file_lines("notfound.txt", "test"):
    print(line.strip())