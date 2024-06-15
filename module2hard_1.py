def get_kod_1(n):
    numbers = list()
    numbers_1 = list()
    _list_result = list()
    for i in range(1, n):
        numbers.append(i)
    for i in range(1,20):
        numbers_1.append(i)
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers_1)):
            if len(numbers_1) > 1:
                _sum_par = numbers[i] + numbers_1[j]
                if n % _sum_par == 0:
                    _list_result.append(numbers[i])
                    _list_result.append(numbers_1[j])
                continue
            numbers_1.remove(numbers_1[j])
    return _list_result


n = int(input('Введите число от 3 до 20: ',))
result = get_kod_1(n)
print(*result, sep="")
