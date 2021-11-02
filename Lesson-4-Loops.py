import time

count = 0
# WHILE
while True:  # бесконечный цикл
    count += 1
    print(count, "- Hello!")
    time.sleep(.200)

# ===========================
while count < 10:
    count += 1
    print(count, "- Hello!")
    time.sleep(.500)

# ===========================

# FOR
for i in range(0, 10):
    print(i)
    time.sleep(.500)

arr = [1, 2, 34, 5, 16, 750, 58, 930, 15, 100]

for i in arr:
    print("Hello,", i)
    time.sleep(.300)

# ===========================
for i in arr:
    multiply_1 = i * 10
    print("multiply_1 =", multiply_1)
    time.sleep(.300)

# ===========================
for i in arr:
    dev_i = i % 10
    if dev_i == 0:
        print("i = ", i, "dev_i =", dev_i)
        time.sleep(.300)

# ===========================
for i in arr:
    if i < 10:
        print("i = ", i)
        time.sleep(.300)

# ===========================
for i in arr:
    print("i =", i)
    if i == 58:
        break
    time.sleep(.200)

# ===========================
for i in arr:
    print("i =", i)
    if i == 58:
        continue
    print("Hello, ", i*10)
    time.sleep(.200)

#  ===========================
count = 1
while True:
    name = input("Enter your name: ")
    print("Hello, ", name, count)

    count += 1

# CURR CALCULATOR ===========================
curr = "USD"
curr_rate = 71.55

while True:
    usd_input = int(input("Enter USD amount: "))
    usd_rub = float(usd_input * curr_rate)
    print("You enter: $", usd_input, "=", usd_rub, "RUB")
