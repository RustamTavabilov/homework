numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:  #for i in range(1, 16):
    a = 0
    for j in range(1, i+1): #len(numbers)+1
        q = numbers[i-1] % j
        if q == 0:
            a = a + 1
    if a == 2:
        primes.append(i)
    elif a > 2:
        not_primes.append(i)
    else:
        continue

print('Primes:', primes)
print('Not Primers:', not_primes)



