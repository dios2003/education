def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(a='Функция с параметрами по умолчанию: ', b='', c='')
print_params(b=25)
print_params(a=47, b=True, c=2)
print_params(c=[1,2,3])
print_params()


values_list = [54.32, 'Строка', True]
values_dict = {'a': True, 'b': '2', 'c': 'строка'}
print_params(a='Распаковка параметров: ', b='', c='')
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(a='Распаковка + отдельные параметры: ', b='', c='')
print_params(*values_list_2, 42)
