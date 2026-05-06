def divisible_3(number):
    return num % 3 == 0
num = int(input("Введите число: "))
if divisible_3(num):
    print("делится на 3")
else:
    print("не делится на 3")