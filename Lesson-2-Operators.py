# арифметические операции
a = 2
b = 5
result = a + b
print("Result =", result)

result = b - a
result = b * a
result = b / a
result = b ** a
result = b // a
result = b % a
print("Result =", result, type(result))

if a % 2 == 0:
    print('Even')
else:
    print('Odd')

print("Result =", result, type(result))

res = 5 + 10 * (2 + 7)**2 + 10/5

# ====================================================================
# операторы присваивания
b = 10
b += 2   # b = b + 2
b -= 2   # b = b - 2
b /= 2   # b = b / 2
b *= 2   # b = b * 2
b //= 2  # b = b // 2
b %= 2   # b = b % 2
print("Result =", b)
# ====================================================================
import math

a = 134.987654
b = math.floor(a)   # Округляет число x вниз
c = math.ceil(a)    # Округляет число x вверх
d = int(a)          # Округляет число в сторону нуля
e = 5

print(a, b, c, d)
print(math.pi)
print(math.factorial(e))

a = 5
b = 2
c = 5 ** 2
cc = int(math.pow(a, b))

print("cc =", cc)
