import csv

file_path = "C:/Users/Nadine/PycharmProjects/Python Basics/"
file_name = "Les-8_headers.csv"
csv_file_name = file_path + file_name

users_list = [
    ["Vadim", 32],
    ["Alexey", 34],
    ["Juliya", 26]
]

users_dict = [
    {"name": "Maxim", "age": 35},
    {"name": "Roman", "age": 23},
    {"name": "Dmitry", "age": 28}
]

with open(csv_file_name, "w") as cf:
    columns = ["name", "age"]
    writer = csv.DictWriter(cf, fieldnames=columns)
    writer.writeheader()

    # writer.writerows(users_list)

    row_1 = {"name": "Vlas", "age": 27}
    writer.writerow(row_1)

with open(csv_file_name, "a") as csv_f:
    columns = ["name", "age"]
    writer = csv.DictWriter(csv_f, fieldnames=columns)

    # row_1 = ["Vlas", 27]

    writer.writerows(users_dict)


with open(csv_file_name, "r") as csv_f:

    reader = csv.DictReader(csv_f)
    line_count = 0

    age_list = []

    for row in reader:
        print(line_count, row["name"], row["age"])

        age_list.append(int(row["age"]))
        line_count += 1

    print(age_list)


