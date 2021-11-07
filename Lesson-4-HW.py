# Циклы While

count = 0           # Создать переменную count со значением 0
range_count = 10    # Создать переменную range_count со значением 10
for_count = 0       # Создать переменную for_count со значением 0
run = True          # Создать переменную run  со значением True

while run:                  # Сделать цикл while, который будет работать пока run
    print("Hello Cycle!")   # 5.1 Выводить в консоль “Hello Cycle”

while run:                     # Сделать цикл while, который будет работать пока run
    print("Step =", count)     # 6.1 Выводить в консоль (“Step =”, count)
    count += 1                 # 6.2 Переменной count прибавлять 1 с присвоением.

while count < range_count:      # Сделать цикл while, который будет работать пока count < range_count
    print("Step =", count)      # 7.1 Выводить в консоль (“Step =”, count)
    count += 1                  # 7.2 Переменной count прибавлять 1 с присвоением.

while count < range_count:                  # Сделать цикл while, который будет работать пока count < range_count
    print("Step =", count)                  # 8.1 Выводить в консоль (“Step =”, count)
    count += 1                              # 8.2 Переменной count прибавлять 1 с присвоением.
    if count == 3:                          # 8.3 Сделать if с условием, если count равен 3,
        print("Step =", count, "If body")   # то выводить в консоль (“Step =”, count, ‘If body’)

while run:                      # Сделать цикл while который будет работать пока run
    print("Step =", count)      # 9.1 Выводить в консоль (“Step =”, count)
    count += 1                  # 9.2 Переменной count прибавлять 1 с присвоением.
    if count == range_count:    # 9.2 Сделать if с условием, если count равен range_count,
        print("STOP =", count)  # то цикл остановится.
        break                   # 9.3 В теле if вывести в консоль (“STOP”, count)


#  Циклы For

for item in range(for_count, range_count):  #  Сделать цикл for c переменной item, который будет работать пока счётчик
    print("Step =", item)     #  range досчитает от for_count до range_count.  10.1 Вывести в консоль (‘Step =’, item)

for item in range(0, 30):       # Сделать цикл for c переменной item, который будет работать пока счётчик range досчитает от 0 до 30
    print("Step =", item)       # 11.1 Вывести в консоль (‘Step =’, item)
    if item == 5:               # 11.2 Сделать if с условием, если item равен 5,
        print("Item =", item)   #      то вывести в консоль (‘Item =’, item).
    if item == 10:              # 11.3 Сделать if с условием, если item равен  10,
        print("Item =", item)   #      то вывести в консоль (‘Item =’, item).
    if item < 4:                # 11.4 Сделать if с условием, если item меньше 4,
        print("Item <", item)   #      то вывести в консоль (‘Item <’, item).
    if item >= 27:              # 11.5 Сделать if с условием, если item больше или равно 27,
        print("Item >=", item)  #       то вывести в консоль (‘Item >=’, item).

for item in range(0, range_count+1):            # Сделать цикл for c переменной item, который будет работать пока счётчик range досчитает от 0 до range_count +1
    print("Step =", item)                       # 12.1 Вывести в консоль (‘Step =’, item)
    if item == 7:                               # 12.2 Сделать if с условием, если item равен  7.
        inner_count = 0                         #    - В теле if создать переменную inner_count равную 0
        print("-- inner_count", inner_count)    # 	 - В теле if вывести в консоль (‘-- inner_count =’, inner_count)
        for inner_item in range(0, item):       # 	 - В теле if сделать ещё одни цикл for с переменной inner_item, который будет работать пока счётчик range досчитает от 0 до item.
            print("-------- Inner_Step =", inner_item)  # 	Тело внутреннего цикла For: -- Вывести в консоль (‘-------- Inner_Step =’, inner_item)
            if inner_item == 5:                         # 	-- Сделать if если inner_item равен 5,
                inner_count = inner_item                #      то в inner_count присвоить inner_item.
        print("-- inner_count =", inner_count)  # 	- За пределами тела предыдущего цикла вывести в консоль (‘-- inner_count =’, inner_count)


for item in range(0, 20):           # Сделать цикл for c переменной item, который будет работать пока счётчик range досчитает от 0 до 20
    print("Step =", item)           # 13.1 Вывести в консоль (‘Step =’, item)
    if 7 < item < 12:               # 13.2 Сделать if с условием, если item больше 7 и item меньше 12.
        print("If_item =", item)    # 	- В теле if вывести (‘If_item =’, item)
        continue                    # 	- В теле if поставить continue
print("End_iteration =", item)      # 13.3 Выйти из if. Вывести в консоль (‘End_iteration =’, item)