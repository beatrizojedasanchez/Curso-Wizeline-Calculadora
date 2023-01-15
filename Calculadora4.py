import math


def calculator():
    while True:
        print("Selecciona la operación")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Raiz")
        print("6. Exponente")
        print("7. Seno")


        choice = input("Ingresa tu elección (1/2/3/4/5/6/7): ")

        if choice == '1':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print(num1, "+", num2, "=", num1 + num2)
        elif choice == '2':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print(num1, "-", num2, "=", num1 - num2)
        elif choice == '3':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print(num1, "*", num2, "=", num1 * num2)
        elif choice == '4':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print(num1, "*", num2, "=", num1 * num2)
        elif choice == '5':
            num1 = float(input("Ingresa el númera para sacar su raiz: "))
            raiz=math.sqrt(num1)
            print("La raiz cuadrada de " + num1 + "es "+ raiz)
            
        else:
            print("Opción inválida")

calculator()

