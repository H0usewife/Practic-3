result = ""
first_slovo = True

while True:
    slovo = input()
    
    if slovo == "stop":
        break
    
    if first_slovo:
        result = slovo
        first_slovo = False
    else:
        result = result + " " + slovo
        
print(result)