# Try и Except

def add_everything_up(a, b):
    try:
        result = a+b
        if isinstance(result, float):
            result = str(f'{result:.{3}f}')
    except TypeError as exc:
        result = str(a) + str(b)
    return result


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
