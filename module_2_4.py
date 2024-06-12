numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()
is_prime = True
for i in range(0, len(numbers)):
    for j in range(2, numbers[i]):
        if numbers[i] % j == 0:
            is_prime = False
    if is_prime:
        if numbers[i] != 1 and numbers[i] != 0:
            primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
    is_prime = True
print('primes: ', primes)
print('not_primes: ', not_primes)
