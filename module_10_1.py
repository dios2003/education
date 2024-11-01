# Потоковая запись в файлы

import threading
from time import sleep
from time import time


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(1, word_count+1):
            file.write(f'Какое-то слово № {i}' + '\n')
            sleep(0.1)
    return print(f'Завершилась запись в файл {file_name}')


start_time = time()
writes_1 = write_words(10,'example1.txt')
writes_2 = write_words(30,'example2.txt')
writes_3 = write_words( 200, 'example3.txt')
writes_4 = write_words(100, 'example4.txt')
end_time = time()
print(f'Работа потоков {end_time - start_time}')

start_time = time()

thread_1 = threading.Thread(target=write_words, args=(10, ), kwargs={'file_name': 'example5.txt'})
thread_2 = threading.Thread(target=write_words, args=(30, ), kwargs={'file_name': 'example6.txt'})
thread_3 = threading.Thread(target=write_words, args=(200, ), kwargs={'file_name': 'example7.txt'})
thread_4 = threading.Thread(target=write_words, args=(100, ), kwargs={'file_name': 'example8.txt'})

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()


thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

end_time = time()
print(f'Работа потоков {end_time - start_time}')
