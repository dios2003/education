first = int(input('Введите первое число :'))
second = int(input('Введите второе число :'))
third = int(input('Введите третье число :'))
if first == second and third == second:
    print(3)
elif first == second or third == second or third == first:
    print(2)
else:
    if not (first == second and third == second and third == first):
        print(0)
