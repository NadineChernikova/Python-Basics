print('Hello, Python QA!')
print('Hello', 'Python', 'QA!')
print('Hello ' + 'Python ' + 'QA!')
print('Hello', 'Python', 'QA!', sep=' ')
# ====================================================================
# комментарии "Ctrl + /"
# ====================================================================
name = input('Input your name: ')  # предложение ввода
print('Hello,', name+'!')  # вывод в консоль
# ====================================================================
name = 'Nadine'  # объявление переменной
name_len = len(name)  # выводит длину строки
sorted_name = sorted(name)  # сортирует строку
name_type = type(name)  # выводит тип данных переменной

print('Name:', name)
print('Len:', name_len)
print('Sorted_name:', sorted_name)
print('Name_type:', name_type)
# ====================================================================
# именование переменных: name, user_name, userName, _name, Name, nAme
# ====================================================================
# зарезервированные слова: True, False, None, if, else, elif, for, while, break, continue, and, or, in, class, return, import
# ====================================================================
# типы данных: string, int, float, boolean(True, False), bytes, list, dict
# str(int) - приведение числа к строке
# int(string), float(string) - приведение строки к числу

name = 'Nadine'
age = 20
print(name + ' ' + str(age))  # конкатенация строк

bool_type_true = True
bool_type_false = False

b_type = bytes(123)
print(b_type)

list_type = ['qwerty', '123', 456, True, ['12e', 34, '65']]
print(list_type[4][1])  # обращается к элементу списка (отсчёт от 0)

tuple_type = tuple[12, '23']

dict_type = {'key1': 12,
             'name_1': 'Nadine',
             'inner_json': {'in_1': 777,
                            'in_2': 'Nadine'}}
print(dict_type['key1'])  # выводит элемент словаря по ключу
print(dict_type['inner_json']['in_2'])
# ====================================================================
