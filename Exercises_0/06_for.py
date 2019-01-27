# Student: Josué Ignacio Cabrera Díaz
# for loops with for exercise
'''
Crear un archivo llamado 06_for.py
        Crear una lista con nombres de persona e incluir, como mínimo, 5 nombres (como mínimo, uno ha de tener la vocal "a")
        Crear una lista llamada "selected"
        Recorrer, mediante un for, la lista de los nombres e imprimir un texto con el nombre recorrido en dicha iterración. Asimismo, si el nombre de esa iteración contine una "a", añadirlo a la lista llamada "selected"
        Finalmente, imprimir por pantalla la lista "selected"
'''
    
input_list = input("Enter five names separated by comma: ")
list_ = input_list.split(",") # formatting the input_list
selected = [] # initializing list

for i in range(len(list_)):
    print(list_[i])
    for letter in list_[i]:
        if letter =="a" or letter == "A" or letter == "á" or letter =="Á":
            selected.append(str(list_[i]))
            break
print("-------")
print(selected)
