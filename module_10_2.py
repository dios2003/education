# Потоки на классах"
# Цель: научиться создавать классы наследованные от класса Thread
# Задача "За честь и отвагу!"

import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100
        self.counter_day = 0

    def timer(self, name, power, enemies):
        while enemies:
            self.counter_day += 1
            enemies -= power
            print(f'{name} сражается {self.counter_day} день(дня), осталось {enemies} воинов.')
            sleep(1)

    def run(self):
        print(f'{self.name} на нас напали')
        self.timer(self.name, self.power, self.enemies)
        print(f'{self.name} одержал победу спустя {self.counter_day} дней(дня)!"')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
first_knight.join()
print('Все битвы закончились!')
