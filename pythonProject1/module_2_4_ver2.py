numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for elem in numbers:
    Flag = True
    for divizor in range(2, elem):
        if elem % divizor == 0:
            Flag = False
            not_primes.append(elem)
            break
    if Flag == True and elem != 1:
        primes.append(elem)

print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')
