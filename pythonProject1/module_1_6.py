my_dict = {'name': 'Rustam' , 'age': 1989 , 'gender': 'male'}
print('Dict:', my_dict)
print('Existing value:' , my_dict['name'])
print('Not existing value:' , my_dict.get('surname'))
my_dict.update({'surname': 'Tavabilov', 'year': 35})
rem = my_dict.pop('age')
print('Deleted value:' , rem)
print(my_dict)
print()

my_set = {15,30,90,30,15,'слон','dog','cat','dog',(5,8,4,5)}
print(my_set)
my_set.update({56,69})
my_set.remove(15)
print(my_set)