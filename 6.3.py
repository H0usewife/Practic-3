def magicDate(date):
    day, month, year = date.split(".")

    day = int(day)
    month = int(month)

    lasttwo = int(year[-2:])

    return day * month == lasttwo


date = input("Введите дату в формате дд.мм.гггг: ")

print(magicDate(date))