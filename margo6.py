# While True:
# password1=int(input("Введите пароль:"))

# if  password1<=8:
#     print("Надежный пароль")
# else:
#     print("")
# password1=int(input("Введите пароль:"))
#  For password1 in range(0,9)
#      print("")
#  else:
#     print("")
While True:

password=int(input("Введите пароль:"))
has_num=any(chr.isdigit)(for char in password)
if len(password)>=8 and has_num:
    print("Принят")
    break
else:
    password=int(input("Введите пароль:"))
