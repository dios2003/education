immutable_var = (1,"Cat", 2, True)
print(immutable_var)
# immutable_var[1] = "Dog"
# Кортеж - неизменямый список элементов
# Кортежи не поддерживают изменение элементов, так как не поддерживается обращение к элементу кортежа.
# Изменяться могут только значения внутри элемента.
mutable_list = [1, 2, 3, 4, 5]
print(mutable_list)
mutable_list = [1, 2, 3, 4, 5] + ["String"]
print(mutable_list)
mutable_list[0] = "Dog"
print(mutable_list)
