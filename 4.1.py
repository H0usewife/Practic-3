while True:
    password = input("Введите пароль: ")
    if len(password1) >= 8:                          
        print("Принят")
        continue
    has_num=False
    for char in password1:
    if chr.isdigit():
        has_num=True
        break
    else:
        password = input("Введите пароль:")
