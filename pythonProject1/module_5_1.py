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

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
