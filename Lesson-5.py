import time
import names
import randomtimestamp as rd
from lesson_5_func import yolochka_3, u_weight

def yolochka_1(item_1, item_2):

    result = item_1 + 100
    result_2 = item_2 + 1000

    print("Hello, youlocka_1!")
    print("item_1 =", item_1)
    print("result =", result, result_2)

#  ======================================

def yolochka_2(y_1):

    result = y_1 + 300

    print("Hello, youlocka_2!")
    print("item_1 =", y_1)
    print("result =", result)


# yolochka_1(10, 20)
# print("==================")
# yolochka_2(5)

#  ======================================

for i in range(0, 10):
    yolochka_2(i)
    time.sleep(.400)
    print("******************")

    yolochka_1(i, i * 2)
    time.sleep(.400)
    print("==================")

#  ======================================

for i in range(0, 10):

    user_name = names.get_full_name()
    gen_date = rd.random_date()
    user_weight = u_weight()

    yolochka_3(user_name, gen_date, user_weight, current_age=45)
    time.sleep(.400)
    print("******************")
