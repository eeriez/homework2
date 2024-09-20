import random

#  lambda
first = 'Мама мыла раму'
second = 'Рамена мало было'

chars_comparison = list(map(lambda x, y: x == y, first, second))
print(chars_comparison)


#  замыкание
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as f:
            for i in data_set:
                f.write(str(i) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


#  __call__
class MysticBall:
    def __init__(self, *words):
        self.words = [*words]

    def __call__(self):
        word = random.choice(self.words)
        return word


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
