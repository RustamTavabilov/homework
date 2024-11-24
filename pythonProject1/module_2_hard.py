#"Слишком древний шифр"
n = int(input("Введите число от 3 до 20: "))
pairs = str(n) + ' - '
for i in range(1, n):
    for j in range(i+1, n-i+1):
        if n % (i + j) == 0:
            pairs = pairs + str(i) + str(j)

print(pairs)