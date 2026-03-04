color1 = input("Введите первый цвет: ")
color2 = input("Введите второй цвет: ")

if color1 == "красный":
    if color2 == "синий":
        print("фиолетовый")
    elif color2 == "желтый":
        print("оранжевый")
    else:
        print("ошибка")
elif color1 == "синий":
    if color2 == "красный":
        print("фиолетовый")
    elif color2 == "желтый":
        print("зеленый")
    else:
        print("ошибка")
elif color1 == "желтый":
    if color2 == "красный":
        print("оранжевый")
    elif color2 == "синий":
        print("зеленый")
    else:
        print("ошибка")
else:
    print("ошибка")