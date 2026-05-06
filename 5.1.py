n=int(input("Введите количество слов:"))
for i in range(n):
    slovo=input("Введите слово:")
    if i == 0: # если это первое слово
        result=slovo
    else:
        result=result+" "+ slovo
        print(result)
