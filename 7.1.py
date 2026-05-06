numbers = [3, 7, 12, 25, 40]

user_number = int(input("Введите число: "))

print("Список чисел:", numbers)
print("Ваше число:", user_number)

if user_number in numbers:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")