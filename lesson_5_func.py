import random


def yolochka_3(u_name, b_date, u_weight, current_age = 30):

    result = "Hello, " + u_name + "! You was born in " + str(b_date) + ". Age = " + str(current_age)
    current_weight = u_weight

    print(result)
    print("Now your weight is", current_weight, "kg")


def u_weight():
    random_int = random.randint(20, 80)
    return random_int
