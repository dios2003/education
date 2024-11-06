# Домашнее задание по теме "Очереди для обмена данными между потоками."
# Цель: Применить очереди в работе с потоками, используя класс Queue.
# Задача "Потоки гостей в кафе":

import threading
from queue import Queue
from time import sleep
from random import randint


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for i in range(0, len(guests)):
            flag = 0
            for j in range(0, len(self.tables)):
                if self.tables[j].guest is None:
                    flag = 1
                    self.tables[j].guest = guests[i]
                    Guest.start(guests[i])
                    Guest.join(guests[i])
                    print(f'{guests[i].name} сел(-а) за стол номер {self.tables[j].number}')
                    break
            if flag == 0:
                self.queue.put(guests[i])
                print(f'{guests[i].name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or True in [self.tables[i].guest is not None for i in range(0, len(self.tables))]:
            for i in range(0, len(self.tables)):
                if self.tables[i].guest is not None and self.tables[i].guest.is_alive() is False:
                    print(f'{self.tables[i].guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {self.tables[i].number} свободен')
                    self.tables[i].guest = None
                if not self.queue.empty() and self.tables[i].guest is None:
                    self.tables[i].guest = self.queue.get()
                    print(f'{self.tables[i].guest.name} вышел(-ла) из очереди и сел(-а) за стол номер'
                          f' {self.tables[i].number}')
                    Guest.start(self.tables[i].guest)
                    Guest.join(self.tables[i].guest)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel',
                'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
