def get_kod(n):
    numbers = list()
    _list_result = list()
    for i in range(1, n):
        numbers.append(i)
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if len(numbers) > 1:
                _sum_par = numbers[i] + numbers[j]
                if n % _sum_par == 0:
                    _list_result.append(numbers[i])
                    _list_result.append(numbers[j])
    return _list_result


n = int(input('Введите число от 3 до 20: ',))
result = get_kod(n)
print(*result, sep="")
