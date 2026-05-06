numbers = [1, 5, 3, 7, 5, 8, 3]

repeats = []

for number in numbers:
    if numbers.count(number) > 1 and number not in repeats:
        repeats.append(number)

if repeats:
    print("Повторяющиеся элементы:", repeats)
else:
    print("Повторяющихся элементов нет")