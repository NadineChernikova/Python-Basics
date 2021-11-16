import json

dict_1 = {}   # создание пустого словаря

dict_item = {     # создание словаря с данными
    1: "Julia",
    2: [1, 2, 3, 4, 5],
    3: {"name": "Alexey", "age": "32", "salary": 10000}
}

print(dict_item)
print(dict_item[2])
print(1, ":", dict_item[1])
print(3, ":", dict_item[3]["name"])

x = dict_item.get(3).get("salary")   # достать элемент
print(x)

dict_item["city"] = "Tokyo"   # добавление элемента
print(dict_item)

dict_item[3]["city"] = "London"   # добавление элемента в дикте.дикте
print(dict_item)

dict_item[1] = "Maxim"   # замена значения в элементе
print(dict_item)

del dict_item[2]  # удаление элемента по ключу
print(dict_item)

dict_item.popitem()   # удаление последнего элемента
print(dict_item)

dict_item.pop(2)   # удаление элемента по ключу
print(dict_item)

dict_item.pop("city")   # удаление элемента по ключу
print(dict_item)

dict_item.clear()   # чистит весь дикт
print(dict_item)

# ============================== копирование
print("dict_item", dict_item)

dict_2 = dict_item
print("dict_2: ", dict_2)

dict_2["city"] = "Mexico"

dict_3 = dict_item
print("dict_3: ", dict_3)

dict_4 = dict_item.copy()
print("dict_4: ", dict_4)

# ============================== итерация
for key, value in dict_item.items():

    print("key", key, "value", value)

print("="*20)

for key in dict_item:

    print("key", key)
    print("item", dict_item[key])

# ===========================  генерация данных
names = ("Vadim", "Dmitry", "Maxim")
salary = 10000

dd = dict.fromkeys(names, salary)
print(dd)

# ===========================  JSON
path = "C:/Users/Nadine/PycharmProjects/Python Basics/"
file_title = "Les-9.json"

full_name = path + file_title

dict_item = {
    1: "Julia",
    2: [1, 2, 3, 4, 5],
    3: {"name": "Alexey", "age": "32", "salary": 10000},
    "city": "Moscow",
    False: "False",

}

with open(full_name, "w") as jf:
    json.dump(dict_item, jf)

with open(full_name, "r") as jf:

     json_data = jf.read()
     json_object = json.loads(json_data)

     print("json_data: ", json_data, type(json_data))
     print("json_object: ", json_object, type(json_object))
     print(json_object["city"])
