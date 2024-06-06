# Словари
my_dict = {'Dmitrii': 1970, "Svetlana": 1985, 'Nastya': 2008}
print(my_dict)
print(my_dict['Svetlana'])
my_dict['Katya'] = 2013
print(my_dict['Katya'])
my_dict['Ksusha'] = 2017
my_dict['Tatyana'] = 1965
del my_dict['Svetlana']
print(my_dict)
# Множества
my_set = {'Svetlana', 'Svetlana', 1985, 2008, 1985, 2013, 1965, 1985, False, False, True,}
print(my_set)
print(my_set.add('Valera'))
print(my_set.add('Roman'))
print(my_set.discard('Svetlana'))
print(my_set)
