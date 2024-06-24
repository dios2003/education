def calculate_structure_sum(*_data):
    _list_data = list(_data)
    _sum = int()
    if len(_list_data) >= 1:
        for i in range(0, len(_list_data)):
            if isinstance(_list_data[i], str):
                _sum += len(_list_data[i])
            elif isinstance(_list_data[i], int):
                _sum += _list_data[i]
            elif isinstance(_list_data[i], list):
                _sum += calculate_structure_sum(*_list_data[i])
            elif isinstance(_list_data[i], dict):
                _sum += calculate_structure_sum(*_list_data[i].items())
            elif isinstance(_list_data[i], tuple):
                _sum += calculate_structure_sum(*_list_data[i])
            elif isinstance(_list_data[i], set):
                _sum += calculate_structure_sum(*_list_data[i])
        return _sum
    return _sum


data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(*data_structure)
print(result)
