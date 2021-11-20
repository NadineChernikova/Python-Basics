import random
import secrets
import names
import russian_names as rn


num = [1, 2, 3]
for i in num:
    print(i)

# =======================================

num2 = list(range(20))
print(num2)

num_even = list(range(2, 20, 2))
print(num_even)

num_even2 = [i for i in range(20) if i % 2 == 0]
print(num_even2)

num_odd = [i for i in range(20) if i % 2 != 0]
print(num_odd)

i = 0
c = ["item_"+str(i) for i in range(10)]
print(c)

name_list = []
for i in range(20):
    j = names.get_full_name()
    name_list.append(j)
print(name_list)

# =======================================

empl = []
for i in range(20):
    n = names.get_full_name()
    a = list(range(18, 90))
    s = list(range(1500, 10000))
    b = secrets.choice(a)
    d = secrets.choice(s)
    l = []
    l.append(n)
    l.append(b)
    l.append(d)
    empl.append(l)

print(empl)

# ================================= russian_names


def ru_names():
    name = rn.RussianNames(count=1, patronymic=False, name_reduction=False)
    name = name.get_batch()
    name = name[0]
    return name


def age():
    age_list = list(range(1, 99))
    for i in range(20):
        a = random.choice(age_list)
        return a


name_age_list = []
for i in range(20):
    person = [ru_names(), age()]
    name_age_list.append(person)

print(name_age_list)

# =================================


def create_names():
    a = []
    for i in range(20):
        name = names.get_full_name()
        a.append(name)
    return a


list_names = create_names()

print(list_names)

# =================================

name = input("What is your name? ")
print("Hello,", name+"!")

# =================================
asd = []


def amount():

    word = input("Word: ")
    count = int(input("Repeat: "))
    for i in range(count):
        asd.append(word + str(i))
    return asd


print(amount())

file = "C:/Users/Nadine/PycharmProjects/Python Basics/new_text.txt"

with open(file, "w") as f:
    writer = f.writelines("\n".join(asd))

# ===================== високосный год


def year():
    i = int(input("Enter a year: "))
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        print("Год високосный!")
    else:
        print("Год не високосный!")
    return i


y = year()





