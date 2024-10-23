# Создание исключений

class Car:

    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.vin = __vin
        self.numbers = __numbers
        Car.__is_valid_vin(__vin)
        Car.__is_valid_numbers(__numbers)

    @staticmethod
    def __is_valid_vin(vin_number):
        result = None
        if isinstance(vin_number, int) and vin_number in range(1000000, 9999999):
            result = True
        if not isinstance(vin_number, int):
            message = 'Некорректный тип vin номер'
            raise IncorrectVinNumber(message)
        if vin_number not in range(1000000, 9999999):
            message = 'Неверный диапазон для vin номера'
            raise IncorrectVinNumber(message)
        return result

    @staticmethod
    def __is_valid_numbers(numbers):
        result = None
        if isinstance(numbers, str) and len(numbers) == 6:
            result = True
        if not isinstance(numbers, str):
            message = 'Некорректный тип данных для номеров'
            raise IncorrectCarNumbers(message)
        if len(numbers) != 6:
            message = 'Неверная длина номера'
            raise IncorrectCarNumbers(message)
        return result


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
    result = False


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
    result = False


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
