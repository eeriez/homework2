import random
from threading import Thread
from time import sleep
from random import randint
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            is_seated = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    is_seated = True
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            if is_seated is False:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        guest_pres = False
        for table in self.tables:
            if table.guest is not None:
                guest_pres = True

        while (self.queue.empty() is False) or (guest_pres is True):
            for table in self.tables:
                if self.queue.empty() is True:
                    break

                if table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()
                    table.guest.join()

                if table.guest.is_alive() is False:
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

                if table.guest is not None:
                    guest_pres = True
                else:
                    guest_pres = False


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
