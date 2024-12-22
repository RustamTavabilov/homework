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

    def __eq__(self, other):
        return self.namber_of_floor == other.namber_of_floor

    def __lt__(self, other):
        return self.namber_of_floor < other.namber_of_floor

    def __le__(self, other):
        return self.namber_of_floor <= other.namber_of_floor

    def __gt__(self, other):
        return self.namber_of_floor > other.namber_of_floor

    def __ge__(self, other):
        return self.namber_of_floor >= other.namber_of_floor

    def __ne__(self, other):
        return self.namber_of_floor != other.namber_of_floor

    def __add__(self, value):
        self.namber_of_floor += value
        return self

    def __radd__(self, value):
        self.namber_of_floor += value
        return self

    def __iadd__(self, value):
        self.namber_of_floor += value
        return self

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
