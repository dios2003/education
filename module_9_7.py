# Декораторы в Python

def is_prime(func):
    def wrapper(*args, **kwargs):
        result_func = func(*args)
        if result_func < 2:
            print('Не принадлежит к простым и составным числам')
            return result_func
        for i in range(2, int(result_func**0.5 + 1)):
            if result_func % i == 0:
                print('Составное')
                break
        else:
            print('Простое')
        return result_func
    return wrapper


@ is_prime
def sum_three(*args):
    sum_args = sum(args)
    return sum_args


result = sum_three(2, 3, 6)
print(result)

result = sum_three(2, 2, 2)
print(result)

result = sum_three(4, 4, 4)
print(result)
