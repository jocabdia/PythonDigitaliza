# Student: Josué Ignacio Cabrera Díaz
# Conditionals Exercises
'''
Crear un archivo llamado 04_if.py
        Crear un script en el que guardéis en una variable un número
        Controlar el tamaño del número en 4 rangos (menor de 20, entre 20 y 39, entre 40 y 59, mayor de 60)
        En cada uno de los casos imprimir por pantalla el número que se haya introducido.
'''
input_number = float(input("Enter a number between 0 to 60: "))

if 0 <= input_number <= 19:
    print("Your number", input_number," is less than 20. ")
elif 20 <= input_number <= 39:
    print("Your number", input_number," is between 20 and 39. ")
elif 40 <= input_number <= 59:
    print("Your number ", input_number," is between 40 and 59. ")
elif 59 <= input_number <= 60:
    print("Your number", input_number," is the last valid range. ")
else:
    print("Your number is out of range.")
