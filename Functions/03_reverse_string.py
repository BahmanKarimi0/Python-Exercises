def reverse_string(string):
    lst = []
    for i in range(len(string) - 1, -1, -1):
        lst.append(string[i])
    return ''.join(lst)


print(reverse_string("bahman"))
print(reverse_string("Python"))
