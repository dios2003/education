# Блокировки и обработка ошибок"
# освоить блокировки потоков, используя объекты класса Lock и его методы.
# Задача "Банковские операции":

import threading
from time import sleep
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            number = randint(50, 500)
            self.balance += number
            sleep(0.001)
            print(f'Пополнение: {number}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
        return self

    def take(self):
        for i in range(100):
            number = randint(50, 500)
            print(f'Запрос на {number}')
            if number <= self.balance:
                self.balance -= number
                sleep(0.001)
                print(f'Снятие: {number}. Баланс: {self.balance}')
            if number > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
        return self


bk = Bank()
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
