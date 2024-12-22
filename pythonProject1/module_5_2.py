#Специальный методы классов
class House:
    def __init__(self, name, namber_of_floor):
        self.name = name
        self.namber_of_floor = namber_of_floor

    def go_to(self, new_floor):
        if self.namber_of_floor > new_floor:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.namber_of_floor

    def __str__(self):
        self.info = f'Название: {self.name}, кол-во этажей: {self.namber_of_floor}'
        return self.info

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2) #не понимаю, почему эта страка именно так работает, почему не нужно указывать str?

print(str(h1))
print(str(h2))

# __len__
print(len(h1))
print(len(h2))

