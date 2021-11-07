import random

numbers_list = []   # пустой список
empty_list = list()  # пустой список
num_list = [1, 2, 3, 4, 5, 6, [77, 88], [100, 100]]
new_list = list(num_list)

sum_list = num_list + new_list

print("num_list =", num_list)
print("new_list =", new_list)
print("sum_list =", sum_list)

# ========================================
list_item = num_list[6]         # забирает элемент из списка
list_in_item = num_list[6][1]   # забирает элемент из списка.списка
list_in_item_from_right = num_list[-1]   # забирает элемент из списка.списка
print(list_item)
print(list_in_item)
print(list_in_item_from_right)

# ========== генерация списков
gen_list = [7] * 6
print(gen_list)

range1_list = list(range(20))  # генерирует последовательный список
range2_list = list(range(10, 20))  # генерирует последовательный список от начала
range3_list = list(range(10, 30, 5))  # генерирует последовательный список от начала с шагом
range4_list = list(range(30, 10, -5))  # генерирует последовательный список с шагом в обратном порядке

print(range1_list)
print(range2_list)
print(range3_list)
print(range4_list)

# ========== итерация списков FOR
range_list = list(range(10))
multi_list = [1, True, 123, 13.5, "Nadine", "123", [22, 33], {1: "1"}, (1, 2, 4)]
print(range_list)
print(multi_list)

for i in range_list:
    print("i =", i)

for n in multi_list:
    print("n =", n, type(n))

for k in range(0, len(multi_list)):
    list_item = multi_list[k]
    print("k =", multi_list[k], type(list_item))

# ========== итерирация списков WHILE
item = 0
while item < len(multi_list):
    list_item = multi_list[item]
    print("item =", list_item, type(list_item))
    item += 1

# ========== сравнение
range_list1 = list(range(5))
range_list2 = [0, 1, 2, 3, 4]

print("range_list1 =", range_list1)
print("range_list2 =", range_list2)

if range_list1 == range_list2:
    print("range_list1 = range_list2 --", range_list1 == range_list2)
else:
    print("range_list1 NOT range_list2")

# ========== добавление элементов в список
names = ["Nadine", "Tim"]
print("names =", names)

names.append("Dim")   # добавление в конец списка
print("names =", names)

names.insert(0, "Oleg")   # добавление в списк на определённый индекс
print("names =", names)

names = ['Oleg', 'Nadine', 'Tim', 'Dim']  # узнать индекс элемента
tim_index = names.index("Tim")
print("Tim index =", tim_index)

add_items = ["Martha", "Frank"]  # добавление списка в список
names.append(add_items)
print("names =", names)

add_items = ["Martha", "Frank"]  # добавление списка в список как элементы
names = names + add_items
print("names =", names)

# ========== удаление элементов в список
names = ['Oleg', 'Nadine', 'Tim', 'Dim', 'Martha', 'Frank']
print("names =", names)

names.pop(5)  # удаление по индексу
print("names =", names)

names.remove("Martha")  # удаление по имени элемента
print("names =", names)

names = ["Someone", "Oleg", "Nadine", "Someone", "Tim", "Dim", "Someone", "Martha", "Frank", "Someone"]

so_count = names.count("Someone")
print("SO_count =", so_count)

for item_name in names:
    if item_name == "Someone":
        names.remove("Someone")
print("names =", names)

for item_name in names:
    if "Someone" in names:
        names.remove("Someone")
print("names =", names)

names = ["Tim", "Someone", "Oleg", "Nadine", "Someone", "Tim", "Dim", "Tim",  "Martha", "Frank", "Tim", "Someone"]
names2 = set(names)  # список уникальных значений
names2.remove("Someone")

print(names2)

# ========== сортировка списка
names = ['Oleg', 'Nadine', 'Tim', 'Dim', 'Martha', 'Frank']
digits = []
rand = random.randint(0, 20)

for i in range(rand):

    d_int = random.randint(0, 20)
    digits.append(d_int)
    print("d_int =", digits)

print("digits NOT SORTED =", digits)
digits.sort()
print("digits SORTED =", digits)

names.sort()
print("Names SORTED =", names)

# ========== нахождение минимального/максимального значения в списке
digits1 = [1, 5, 4, 7, 3, 66, 76543, 45, 5, 98, 46, 2, 84, 8754, 0]
print("digits1 =", digits1)

min_digits1 = min(digits1)
max_digits1 = max(digits1)

print("min-digit = ", min_digits1)
print("max-digit = ", max_digits1)

# ========================== генерация списка случайных уникальных чисел ((от, до), кол-во)
ii = random.sample(range(1, 100), 10)
print(ii)
