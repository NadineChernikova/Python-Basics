import random
"""
Python HW 5 Functions, Lists
 - Любой начальный список минимум 70 элементов.(Есть задания где можно меньше, по усмотрению)
 - Все результаты выводить в консоль.
"""

# 1. Написать скрипт, который в создаст список целых чисел.
list1 = list(range(72))
print("1. =", list1, len(list1))

# 2. Написать скрипт, который в создаст список целых чётных чисел.
list_even = list(range(0, 71, 2))
print("2. =", list_even)

# 3. Написать скрипт, который в создаст список целых нечётных чисел.
list_odd = list(range(1, 72, 2))
print("3. =", list_odd)

# 4. Написать скрипт, который из списка целых чисел выведет чётные числа.
list4 = list()
for i in list1:
    if i % 2 == 0:
        list4.append(i)
print("4. =", list4)

# 5. Написать скрипт, который из списка целых чисел выведет нечётные числа.
list5 = list()
for i in list1:
    if i % 2 != 0:
        list5.append(i)
print("5. =", list5)

# 6. Написать скрипт, который из списка целых чисел выведет чётные числа, которые делятся на 5 без остатка.
list6 = list()
for i in list1:
    if i % 2 == 0 and i % 5 == 0:
        list6.append(i)
print("6. =", list6)

# 7. Написать скрипт, который из списка целых чисел выведет количество чётных чисел, которые делятся на 5 без остатка.
list6 = list()
for i in list1:
    if i % 2 == 0 and i % 5 == 0:
        list6.append(i)
print("7. =", len(list6))

# 8. Написать скрипт, который в создаст список целых рандомных чисел.
list8 = random.sample(range(1, 100), 70)
print("8. =", list8, len(list8))

# 9. Написать функцию, которая, получив на вход любой из выше созданных списков, разобьёт его на списки по 5 элементов.
list9 = []


def func9(l):
    temp_list = []
    count = 0
    for i in l:
        count += 1
        if count < 5 and count <= len(l):
            temp_list.append(i)
        else:
            temp_list.append(i)
            list9.append(temp_list)
            temp_list = []
            count = 0


func9(list8)
print("9.1 =", list9, len(list9))


def list_split(n, size):

    for x in range(0, len(n), size):
        yield n[x:x + size]


print("9.2 =", list(list_split(list8, 5)))

# 10. Написать функцию, которая, получив на вход список целых чисел, вернёт 2 списка, список чётных и список нечётных чисел.
list10_even = list()
list10_odd = list()


def even_odd(n):
    for i in n:
        if i % 2 == 0:
            list10_even.append(i)
        else:
            list10_odd.append(i)


even_odd(random.sample(range(1, 100), 70))

print("10.even =", list10_even)
print("10.odd  =", list10_odd)


def func10(n):
    result = ([], [])
    for x in n:
        result[x % 2].append(x)
    return result


(even, odd) = func10(random.sample(range(1, 100), 70))

print("10-even =", even)
print("10-odd  =", odd)

# 11. Написать скрипт, который сгенерирует список под названием 5_stars из списков по 5 элементов целых чисел.
stars_5 = list()
count = 0
while count < 10:
    stars_5_item = list(random.sample(range(0, 40), 5))
    stars_5.append(stars_5_item)
    count += 1

print("11. = ", stars_5)

# 12. Написать скрипт, который выведет список из сумм каждого внутреннего списка из  5_stars
sum_5 = list()
item = 0
while item < len(stars_5):
    list_item = sum(stars_5[item])
    sum_5.append(list_item)
    item += 1

print("12.1 = ", sum_5)

sum_stars = list(map(sum, stars_5))
print("12.2 = ", sum_stars)

"""
13. Написать функцию которая на вход получает список 5_stars, а вернёт 2 списка.
В одном списке внутренние списки из 5_stars сумма чисел которых >= 100, а другой сумма чисел которых < 100.
Если какого-то списка не получится, то вместо него вернуть текст “No lists”
"""
list101 = []
list99 = []


def func13(k):
    item = 0
    while item < len(k):
        list_item = sum(k[item])
        if list_item >= 100:
            list101.append(list_item)
        elif list_item < 100:
            list99.append(list_item)
        item += 1
    if len(list101) != 0:
        print("13.>100 =", list101)
    else:
        print("13. No lists")
    if len(list99) != 0:
        print("13.<100 =", list99)
    else:
        print("13. No lists")


func13(stars_5)



