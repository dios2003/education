# Домашнее задание по теме "Многопроцессное программирование"
# Цель: понять разницу между линейным и многопроцессным подходом, выполнив операции обоими способами.
# Задача "Многопроцессное считывание".

from time import time
from multiprocessing import Pool
from multiprocessing import cpu_count
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()


filenames = [f'./file {number}.txt' for number in range(1, 5)]
# Линейный вызов
# start_time = time()
# for i in range(0, len(filenames)):
    # read_info(filenames[i])
# end_time = time()
# work_time = datetime.timedelta(seconds=end_time - start_time)
# print(f'{work_time} (линейный)')

# Многопроцессный
if __name__ == '__main__':
    start_time = time()
    with Pool(cpu_count()) as pool:
        pool.map(func=read_info, iterable=filenames)
        end_time = time()
    work_time = datetime.timedelta(seconds=end_time - start_time)
    print(f'{work_time} (многопроцессный)')
