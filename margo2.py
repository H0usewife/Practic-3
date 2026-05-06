print("Сколько стоит одна конфета")
candy1=int(input())
print("Сколько конфет ты хочешь купить")
candy2=int(input())

allcandy=candy1*candy2
ves=25*candy2
bag=(ves+100-1)//100

#вывод
print(f"Одна конфета стоит: {candy1}") 
print(f"Ты выбрал {candy2} конфет")
print(f"Общая стоимость: {allcandy}")
print(f"Общий вес: {ves}")
print(f"Кол-во пакетов: {bag}")
