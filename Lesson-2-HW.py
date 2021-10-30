# Arithmetic
import math
#  1. Создать переменную int1 типа integer.
int1 = 35
#  2. Создать переменную int2 типа integer.
int2 = 25
#  3. Создать переменную result_sum в которой вы суммируете int1 и int2.
result_sum = int1 + int2
#  4. Вывести result_sum в консоль.
print("4. Addition result =", result_sum)
#  5. Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.
result_subtr = int1 - int2
#  6. Вывести result_subtr в консоль.
print("6. Subtraction result =", result_subtr)
#  7. Создать переменную result_multi в которой вы умножаете int1 на int2.
result_multi = int1 * int2
#  8. Вывести result_multi в консоль.
print("8. Multiplication result =", result_multi)
#  9. Создать переменную result_exp в которой вы int1 возводите в степень int2.
result_exp = int1 ** int2
#  10. Вывести result_exp в консоль.
print("10. Exponent result =", result_exp)
#  11. Создать переменную result_m_exp в которой вы int1 возводите в степень int2 используя библиотеку math.
result_m_exp = math.pow(int1, int2)
#  12. Вывести result_m_exp в консоль.
print("12. math.Exponent result =", result_m_exp)
#  13. Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item
result_s_root = int2 ** 0.5
#  14. Вывести result_s_root в консоль.
print("14. SquareRoot result =", result_s_root)
#  15. Создать переменную result_m_s_root,
#  в которой вы найдёте квадратный корень любой из переменной int используя библиотеку math.
result_m_s_root = math.sqrt(int2)
#  16. Вывести result_m_s_root в консоль.
print("16. math.SquareRoot result =", result_m_s_root)
#  17. Создать переменную result_mp_s_root,
#  в которой вы найдёте квадратный корень любой из переменной int, используя библиотеку math используя метод pow.
result_mp_s_root = math.pow(int2, 0.5)
#  18. Вывести result_mp_s_root в консоль.
print("18. math.pow.SquareRoot result =", result_mp_s_root)
#  19. Присвоить переменной int1 odd значение
int1 = 45
#  20. Присвоить переменной int2 even значение
int2 = 10
#  21. Создать переменную result_division в которой вы разделите int1 на int2.
result_division = int1 / int2
#  22. Вывести result_division в консоль.
print("22. Division result =", result_division)
#  23. Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего, чем result_division.
result_m_floor = math.floor(result_division)
#  24. Вывести result_m_floor в консоль.
print("24. math.floor result =", result_m_floor)
#  25. Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего, чем result_division.
result_m_ceil = math.ceil(result_division)
#  26. Вывести result_m_ceil в консоль.
print("26. math.ceil result = ", result_m_ceil)
#  27. Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
result_int = int(result_division)
#  28. Вывести result_int в консоль.
print("28. Int result =", result_int)
#  29. Создать переменную result_no_division_loss, в которой вы разделите int1 на int2 без остатка.
result_no_division_loss = int1 // int2
#  30. Вывести result_no_division_loss в консоль.
print("30. Floor Division result =", result_no_division_loss)
#  31. Создать переменную result_division_loss, в которой вы найдёте остаток от деления int1 на int2.
result_division_loss = int1 % int2
#  32. Вывести result_division_loss в консоль.
print("32. Modulus result =", result_division_loss)
#
# Дальше будет реализация через арифметические действия с присваиванием.
#
#  33. Создать переменную int3 и присвоить ей целое число
int3 = int(20.654)
#  34. Прибавить 10 к int3 с присвоением.
int3 += 10
#  35. Вывести int3 в консоль.
print("35. Int3 + 10 =", int3)
#  36. Отнять 5 от int3 с присвоением.
int3 -= 5
#  37. Вывести int3 в консоль.
print("37. Int3 - 5 =", int3)
#  38. Умножить int3 на 3 с присвоением.
int3 *= 3
#  39. Вывести int3 в консоль.
print("39. Int3 * 3 =", int3)
#  40. Разделить int3 на 2 с присвоением.
int3 /= 2
#  41. Вывести int3 в консоль.
print("41. Int3 / 2 =", int3)
#  42. Возвести в степень 2 int3 с присвоением.
int3 **= 2
#  43. Вывести int3 в консоль.
print("43. Int3 ** 2 =", int3)
#  44. Найти квадратный корень int3 с присвоением.
int3 **= 0.5
#  45. Вывести int3 в консоль.
print("45. SquareRoot(Int3) =", int3)
#  46. Присвоить остаток от деления int3
int3 %= 2
#  47. Вывести int3 в консоль.
print("47. Modulus(Int3, 2) =", int3)
#
# Boolean
#
#  48. Создать переменную boolT и присвоить True
boolT = True
#  49. Создать переменную boolF и присвоить False
boolF = False
#  50. Создать переменную boolSum и присвоить сумму boolT и boolF
boolSum = boolT + boolF
#  51. Вывести boolSum в консоль.
print("51. Boolean Addition result =", boolSum)
#  52. Создать переменную boolSubtr и присвоить разницу boolT и boolF
boolSubtr = boolT - boolF
#  53. Вывести boolSubtr в консоль.
print("53. Boolean Subtraction result =", boolSubtr)
#  54. Создать переменную boolMulti и присвоить умножение boolT и boolF
boolMulti = boolT * boolF
#  55. Вывести boolMulti в консоль.
print("55. Boolean Multiplication result =", boolMulti)
#  56. Создать переменную boolDivision и присвоить деление boolT и boolF
# boolDivision = boolT / boolF
#  57. Вывести boolDivision = boolT / boolF в консоль. (Получить ошибку)
# print("57. Boolean Division result =", boolDivision)
#  58. Создать переменную bool1_int и присвоить явное приведение boolT к int
bool1_int = int(boolT)
#  59. Вывести bool1_int в консоль.
print("59. True-to-Int = ", bool1_int)
#  60. Создать переменную bool2_int и присвоить явное приведение boolF к int
bool2_int = int(boolF)
#  61. Вывести bool2_int в консоль.
print("61. False-to-Int = ", bool2_int)
