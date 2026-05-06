def lucky_ticket(ticket):
    
    half = len(ticket) // 2 #Здесь нахожу средеину строки 

    first_half = ticket[:half]
    second_half = ticket[half:]

    sum1 = sum(int(digit) for digit in first_half)
    sum2 = sum(int(digit) for digit in second_half)

    return sum1 == sum2


ticket = input("Введите номер билета: ")

if lucky_ticket(ticket):
    print("Счастливый билет")
else:
    print("Не счастливый билет")