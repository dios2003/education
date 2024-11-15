# Домашнее задание по теме "Обзор сторонних библиотек Python"

import requests
import json
import numpy as np
import pandas as pd
import time
from PIL import Image



def state_response():
    response = True
    # request.get - запрос для получения данных c сервера.
    print('Погода в Москве на завтра request.get')
    url = 'https://api.open-meteo.com/v1/forecast'
    params = {'latitude': 55.45, 'longitude': 37.36,
                      'daily':'sunrise,sunset,temperature_2m_min,temperature_2m_max,precipitation_sum',
                      'timezone': 'Europe/Moscow'}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        tomorrow_sunrise = data['daily']['sunrise'][1]
        tomorow_sunset = data['daily']['sunset'] [1]
        tomorrow_temp_min = data['daily']['temperature_2m_min'][1]
        tomorrow_temp_max = data['daily']['temperature_2m_max'][1]
        tomorrow_precipitation = data['daily']['precipitation_sum'][1]
        print(f'Восход: {tomorrow_sunrise}')
        print(f'Закат: {tomorrow_sunrise}')
        print(f'Минимальная температура: {tomorrow_temp_min}°C')
        print(f'Максимальная температура: {tomorrow_temp_max}°C')
        print(f'Ожидаемое количество осадков: {tomorrow_precipitation} мм' + '\n')
    else:
        print(f'Ошибка {response.status_code}')

    # request.post для отправки данных на сервер погоды
    print('Погода в Москве сегодня request.post:')
    params = {'latitude': 55.45, 'longitude': 37.36, 'forecast_days': 1,
              'daily': 'sunrise,sunset,temperature_2m_min,temperature_2m_max,precipitation_sum',
              'timezone': 'Europe/Moscow'}
    response = requests.post(url='https://api.open-meteo.com/v1/forecast', data=params)
    if response.status_code == 200:
        data_1 = response.json()
        tomorrow_sunrise = data_1['daily']['sunrise'][0]
        tomorow_sunset = data_1['daily']['sunset'][0]
        tomorrow_temp_min = data_1['daily']['temperature_2m_min'][0]
        tomorrow_temp_max = data_1['daily']['temperature_2m_max'][0]
        tomorrow_precipitation = data_1['daily']['precipitation_sum'][0]
        print(f'Восход: {tomorrow_sunrise}')
        print(f'Закат: {tomorrow_sunrise}')
        print(f'Минимальная температура: {tomorrow_temp_min}°C')
        print(f'Максимальная температура: {tomorrow_temp_max}°C')
        print(f'Ожидаемое количество осадков: {tomorrow_precipitation} мм' + '\n')
    else:
        print(f'Ошибка {response.status_code}')

#request.post для отправки изображений на сервер
    print(f'Добавляем изображения на сайт')
    images = ['dog.png', 'tiger.jpg']
    for i in range(0, len(images)):
        img = Image.open(images[i])
        img.show()
        url = 'https://httpbin.org/post'
        multiple_files = [('images', ('dog.png', open('dog.png', 'rb'), 'image/png')),
                      ('images', ('tiger.jpg', open('tiger.jpg', 'rb'), 'image/png'))]
    response = requests.post(url, files=multiple_files)
    time.sleep(5)
    print(f'Код состояния {response}' + '\n')

    # requests.options описывает параметры связи для целевого ресурса, идентифицируемого по заданному URL-адресу
    response = requests.options('https://api.open-meteo.com/v1/forecast')
    print(f'{response.headers} '+ '\n')

def num_py():
    # Работа с одномерными и двумерными массивами, преобразование типов
    list_1 = [10,100, 1000.]
    list_2 = [[1.,2.,3.],[4.,5.,6.]]
    array_1 = np.array(list_1)
    array_2 = np.array(list_2)

    print(type(array_1), array_1)
    print(type(array_2), array_2)
    list_1 = []
    for i in range(0, len(array_1)):
        print(int(array_1[i]))
        list_1.append(int(array_1[i]))
    print(list_1)
    list_1 = []
    for i in range(0, len(array_1)):
        print(float(array_1[i]))
        list_1.append(float(array_1[i]))
    print(list_1)

    # Векторизация, транслирование, универсальные функции
    print(array_2)
    print(array_2 + 1) # векторизация
    print(array_2 * array_1) # транслирование
    print(array_2 * array_2) # векторизация
    print(np.sqrt(array_2)) # универсальная функция

    # Генерация массивов
    print(np.arange(2 * 5).reshape(2, 5)) # 2 строки, 5 столбцов

def pan_das():
    sheet_xlsx =  pd.read_excel("parts.xlsx", "TDSheet")
    sheet_xlsx = sheet_xlsx.sort_values(['Производитель', 'Артикул'])
    sheet_xlsx['Сумма продаж'] = sheet_xlsx['Цена продажи'] * sheet_xlsx['Количество']
    sheet_xlsx['Профит'] = sheet_xlsx['Сумма продаж'] - sheet_xlsx['Себестоимость'] * sheet_xlsx['Количество']
    sheet_xlsx = sheet_xlsx._append({'Производитель':'','Артикул':'', 'Номенклатура':'',
                                     'Себестоимость':'','Цена продажи':'','Количество': '',
                                     'Сумма продаж': sheet_xlsx['Сумма продаж'].sum(),
                                     'Профит': sheet_xlsx['Профит'].sum()}, ignore_index=True)
    print(sheet_xlsx)
    sheet_xlsx.to_excel('parts1.xlsx', sheet_name='TDSheet', index=False)
    sheet_xlsx = pd.pivot_table(sheet_xlsx, values= ['Профит','Сумма продаж'], index='Производитель', aggfunc='sum')
    print(sheet_xlsx)
    sheet_xlsx.to_excel('parts2.xlsx', sheet_name='По категориям', index=True)



example_requests = state_response()
example_numpy = num_py()
example_pandas = pan_das()
