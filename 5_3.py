class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-вол этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House) is True:
            if self.number_of_floors == other.number_of_floors:
                return True
            else:
                return False
        else:
            return 'Incomparable'

    def __ne__(self, other):
        if isinstance(other, House) is True:
            if self.number_of_floors != other.number_of_floors:
                return True
            else:
                return False
        else:
            return 'Incomparable'

    def __add__(self, value):
        if isinstance(value, int) is True:
            self.number_of_floors += value
            return self
        else:
            return 'Incompatible'

    def __radd__(self, value):
        if isinstance(value, int) is True:
            return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int) is True:
            return self.__add__(value)

    def __sub__(self, value):
        if isinstance(value, int) is True:
            self.number_of_floors -= value
            return self
        else:
            return 'Incompatible'

    def __gt__(self, other):
        if isinstance(other, House) is True:
            return self.number_of_floors > other.number_of_floors
        else:
            return 'Incomparable'

    def __ge__(self, other):
        if isinstance(other, House) is True:
            return self.number_of_floors >= other.number_of_floors
        else:
            return 'Incomparable'

    def __lt__(self, other):
        if isinstance(other, House) is True:
            return self.number_of_floors < other.number_of_floors
        else:
            return 'Incomparable'

    def __le__(self, other):
        if isinstance(other, House) is True:
            return self.number_of_floors <= other.number_of_floors
        else:
            return 'Incomparable'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
