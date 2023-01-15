#Libreria
import math
import numpy as np

#Se declaran funciones y variables
def suma():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    print(num1, "+", num2, "=", num1 + num2)

def resta():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    print(num1, "-", num2, "=", num1 - num2)

def division():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    print(num1, "/", num2, "=", num1 / num2)

def multiplicacion():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    print(num1, "*", num2, "=", num1 * num2)

def raiz():
    num1 = float(input("Ingresa el númera para sacar su raiz: "))
    raiz=math.sqrt(num1)
    print("La raiz cuadrada de ",  num1,  " es ",  raiz)

def exponente():
    base = float(input("Ingresa la base: "))
    exponente = float(input("Ingresa el exponente: "))
    resultado=math.pow(base, exponente)
    print("El resultado de ",  base,  "elevado al ",  exponente, "es ", resultado )

def seno():
    num1 = float(input("Ingresa el número: "))
    resultado=np.sin(np.deg2rad(num1))
    print("El seno de " , num1, "es ", resultado )


def calculadora():
    #Se genera menú
    while True:
        print("Selecciona la operación")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Raiz")
        print("6. Exponente")
        print("7. Seno")



#Evaluación de operacion
        operacion = input("Ingresa tu elección (1/2/3/4/5/6/7): ")

        if operacion == '1':
            suma()    
        elif operacion == '2':
            resta()
        elif operacion == '3':
            multiplicacion()
        elif operacion == '4':
            division()
        elif operacion == '5':
            raiz()
        elif operacion == '6':
            exponente()
        elif operacion == '7':
            seno()
                 
        else:
            print("Opción inválida")

calculadora()

