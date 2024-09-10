immutable_var = (1, 2, 3, True, 'Stanislav')
print(immutable_var)
# immutable_var [4] = 200 # при назначении символу 4 значения 200 выскакивает ошибка,
                          # которая показывает что кортеж не поддерживает изменение элемента
# print(immutable_var)
mutable_list = ['Aleksandr', 'Natalia', 'Konstantin']
print(mutable_list[1])
mutable_list[1] = 'Kirill'
print(mutable_list)