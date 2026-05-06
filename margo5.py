while True:
num1=input("Введите пароль:")
has_num= range(0,9)
if len(num1)>=8 and has_num:
    print("Принят")
break
else:
    num1=input("Введите пароль:")