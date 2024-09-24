import random
from threading import Lock, Thread
from time import sleep


class Bank:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            deposit = random.randint(50, 500)
            self.balance += deposit
            print(f'Пополнение: {deposit}. Баланс: {self.balance}')
            print(f'Пополнение {i}')
            if self.balance >= 500 and self.lock.locked() is True:
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            withdraw = random.randint(50, 500)
            print(f'Запрос на {withdraw}')
            if self.balance < withdraw:
                print('Запрос отклонён, недостаточно средств.')
                self.lock.acquire()
            else:
                self.balance -= withdraw
                print(f'Снятие: {withdraw}. Баланс: {self.balance}')
                print(f'Снятие {i}')


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
