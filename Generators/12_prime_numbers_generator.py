def prime_numbers():
    n = 2
    while True:
        is_prime = True
        if n == 2:
            is_prime = True
        elif n % 2 == 0:
            is_prime = False
        else:
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    is_prime = False
        if is_prime:
            yield n
        n += 1


primes = prime_numbers()
for _ in range(6):
    print(next(primes))
