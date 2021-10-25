# 1) Создать переменную типа String
stringVar = "Some string type variable"

# 2) Создать переменную типа Integer
intVar = 46

# 3) Создать переменную типа Float
floatVar = 3.14

# 4) Создать переменную типа Bytes
byteVar = bytes(10)

# 5) Создать переменную типа List
listVar = ["l", "i", "s", "t", "V", "a", "r"]

# 6) Создать переменную типа Tuple
tupleVar = ("t", "u", "p", "l", "e")

# 7) Создать переменную типа Set
setVar = {"s", "e", "t"}

# 8. Создать переменную типа Frozen set
frozensetVar = frozenset("frozenset")

# 9) Создать переменную типа Dict
dictVar = {"dict_id": 1,
           "book": "The Better Angels of Our Nature",
           "author": "Steven Pinker",
           "stock": True}

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
varStorage = [stringVar, intVar, floatVar, byteVar, listVar, tupleVar, setVar, frozensetVar, dictVar]

for i in varStorage:
    print(type(i), ":", i)

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
stringOne = "First"
stringTwo = "Second"
stringConcat = stringOne+stringTwo
print(stringConcat)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(stringVar, intVar)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(stringVar + " " + str(intVar))
