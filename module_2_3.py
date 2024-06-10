my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = int(0)
while not (n == len(my_list) + 1):
    n = n + 1
    if my_list[n-1] >= 0:
        print(my_list[n-1])
        continue
    elif my_list[n-1] < 0:
        break
