numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for elem in numbers:
    chet_deliyel = 0 #счетчик. По определению: Просто́е число́ — натуральное число, имеющее ровно два различных натуральных делителя. С помощью этого счетчика считаю кол-во делителей.
    for divizor in range(1, elem + 1):
        ostatok = numbers[elem - 1] % divizor
        if ostatok == 0:
            chet_deliyel = chet_deliyel + 1 #счётчик делителей без остатка
    if chet_deliyel == 2:
        primes.append(elem)
    elif chet_deliyel > 2:
        not_primes.append(elem)
    else:
        continue

print('Primes:', primes)
print('Not Primes:', not_primes)



