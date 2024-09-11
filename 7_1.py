class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products'

    def get_products(self):
        file = open(self.__file_name, 'r')
        line = file.read()
        file.close()
        return line

    def add(self, *products):
        for i in products:
            file = open(self.__file_name, 'r')
            is_present = False
            if str(i) in file.read():
                is_present = True
            else:
                is_present = False
            file.close()
            file = open(self.__file_name, 'a')
            if is_present is True:
                print(f'Продукт {str(i)} уже есть в магазине.')
            else:
                file.write(f'{str(i)}\n')
            file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
