def divide(number):
    return 100 / number


try:
    number = float(input("Введите число: "))
    result = divide(number)
    print("Результат:", result)

except ValueError:
    print("Ошибка: введено не число.")

except ZeroDivisionError:
    print("Ошибка: деление на ноль невозможно.")

except Exception as error:
    print("Произошла ошибка:", error)