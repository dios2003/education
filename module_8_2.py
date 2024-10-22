# Сложные моменты и исключения в стеке вызовов функции

def personal_sum(numbers):
    result_ps = 0
    incorrect_data = 0
    try:
        for i in range(0, len(numbers)):
            try:
                result_ps += numbers[i]
            except TypeError:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {numbers[i]}')
    except TypeError:
        result_ps += numbers
    result = (result_ps, incorrect_data)
    return result


def calculate_average(numbers):
    result_ps = personal_sum(numbers)
    try:
        len_numbers = len(numbers)
        try:
            result = result_ps[0]/(len_numbers - result_ps[1])
        except ZeroDivisionError:
            result = 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        result = None
    return result


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
