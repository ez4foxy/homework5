immutable_var = (1, 66, "Ханна", True)
print(immutable_var)
# immutable_var[0] = 3
# print(immutable_var)  Кортеж не поддерживает функцию изменения списка
mutable_list = ["Флэм", 5, True]
mutable_list[0] = False
mutable_list[1] = 11
mutable_list[2] = "Тараскус"
print(mutable_list)