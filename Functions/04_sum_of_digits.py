def sum_of_digits(num):
    sum_digits = 0
    while num > 0:
        digit = num % 10
        sum_digits += digit
        num //= 10
    return sum_digits


print(sum_of_digits(5))
print(sum_of_digits(12340))
print(sum_of_digits(70891))
