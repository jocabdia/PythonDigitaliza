# Student: Josué Ignacio Cabrera Díaz
# Calculator Exercises
'''
Crear un archivo llamado 05_calculator.py
        Crear las sentencias necesarias para recoger dos números a través del terminal
        Integrar funcionalidades de suma, multiplicación, división, y exponencial
        Permitir escoger el modo de operación de forma manual (el usuario ha de introducir un número para que sepa qué operación realizar)
        Realizar las operaciones e imprimir el valor por pantalla
'''
print("Primitive integer calculator: Choose first the operation please:")
operation = int(input("Select 1 for addition, 2 for multiplication, 3 for division, 4 for exponentiation: "))

if operation == 1:
    print("You have selected Addition")
    operand_1 = int(input("Enter first operand: "))
    operand_2 = int(input("Enter second operand: "))
    print("The result of adding ", operand_1," and",operand_2, " is: ", operand_1 + operand_2  )
elif operation == 2:
    print("You have selected Multiplication")
    operand_1 = int(input("Enter first operand: "))
    operand_2 = int(input("Enter second operand: "))
    print("The result of multiply ", operand_1," by ",operand_2, " is: ", operand_1 * operand_2  )
elif operation == 3:
    print("You have selected Division")
    operand_1 = int(input("Enter first operand: "))
    operand_2 = int(input("Enter second operand: "))
    print("The result of divide ", operand_1," between ",operand_2, " is: ", operand_1 // operand_2  )
elif operation == 4:
    print("You have selected Exponentiation")
    operand_1 = int(input("Enter first operand: "))
    operand_2 = int(input("Enter second operand: "))
    print("The result of raise ", operand_1," to ",operand_2, " is: ", operand_1 ** operand_2  )
else: 
    print("You must choose a valid operation")
