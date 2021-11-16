import csv

file_path = "C:/Users/Nadine/PycharmProjects/Python Basics/"

# ===== TXT ============================
file_name = "Les-7.txt"

file_path_name = file_path + file_name
print(file_path_name)

f = open(file_path_name, "w")
f.write("Hello, Python!")

f.close()

with open(file_path_name, "w") as txt_file:     # write

    name = "Nadine "
    surname = "Chernikova\n"
    full_name = name + surname

    txt_file.write(full_name)


with open(file_path_name, "a") as txt_file:     # add

    name = "\nTim "
    surname = "Chernikov"
    full_name = name + surname

    txt_file.write(full_name)


with open(file_path_name, "a") as txt_file:     # add через input

    name = input("name: ")
    surname = input("surname: ")
    full_name = "\n" + name + surname + "\n"

    txt_file.write(full_name)

names_list = ["Nadine", "Juliya", "Tanya", "Dmitry"]

with open(file_path_name, "w") as txt_file:

    for i in names_list:
        txt_file.write(i)
        txt_file.write("\n")


with open(file_path_name, "w") as txt_file:

    txt_file.write("\n".join(names_list))

with open(file_path_name, "r") as txt_file:     # read

    read_f = txt_file.read()
    read_f = txt_file.readlines()

    for i in read_f:
        print(i.rstrip(), type(i))


# ===== CSV ============================

file_name = "Les-7.csv"
csv_file_name = file_path + file_name

users_list = [
    ["Vadim", 32],
    ["Alexey", 34],
    ["Juliya", 26]
]

new_users_list = []

for item in range(0, 100):

    for ul_item in users_list:
        name_age = []

        new_name = ul_item[0] + "_" + str(item)

        new_age = 10 + item
        name_age.append(new_name)
        name_age.append(new_age)
        print(name_age)
        new_users_list.append(name_age)
        # users_list.append(name_age)
# users_list.append(new_users_list)


print(new_users_list)

#     users_list.append(name_age)
#
# print(users_list)


with open(csv_file_name, "w") as cf:
    writer = csv.writer(cf, lineterminator='\n')


    writer.writerows(new_users_list)
