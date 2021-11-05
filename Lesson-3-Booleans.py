a = True
b = False

x = 10
y = 5
z = x == y
z = x != y
z = x > y
z = x < y
z = x <= y
z = x >= y
print("Z result =", z)

age = 35
weight = 65
salary = 1000
and_result = age == 35 and weight == 65  # True AND True = True
or_result = age == 35 or weight == 65  # True OR False = True
or2_result = age == 35 or weight == 64 and salary == 1000  # True OR (False AND True) = True
not_result = not age == 35 or not weight == 65 and salary == 1000
print("AND_Result =", and_result)
print("OR_Result =", or_result)
print("OR_Result =", or2_result)
print("NOT_Result =", not_result)


if True:
    print("True: ", True)
else:
    print("Else!!!")

if age == 38:
    print("age = 35:", True)
elif weight == 67:
    print("weight = 65:", True)
elif weight > 55:
    if salary == 1000:
        print("Salary = 1000:", True)
    print("weight > 55:", True)
else:
    print("Else")

