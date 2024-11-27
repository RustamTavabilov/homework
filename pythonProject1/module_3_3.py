def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print('Упражнение 1')
#Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов
print_params()
print_params('a')
print_params('a', 2)
print_params('a', 2, 3)

print()
#Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b = 25)
print_params(c = [1,2,3])

print()
print('Упражнение 2')
values_list = ['буквы', 10189, [10.9, 0.1]]
values_dict = {'a': 2, 'b': 'слово', 'c': False}
#Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)

print()
print('Упражнение 3')
values_list_2 = ['Кукуруза', 89]
print_params(*values_list_2, 42)