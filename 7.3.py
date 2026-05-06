week_days = (
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье"
)

count = int(input("Сколько выходных дней Вы хотите? "))

weekends = list(week_days[-count:])
work_days = list(week_days[:-count])

print("Ваши выходные дни:", weekends)
print("Ваши рабочие дни:", work_days)