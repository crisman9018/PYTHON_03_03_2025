# Ejemplo: funciones
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calculadora(operacion):
    match operacion:
        case "sumar":
            resultado = sumar(a, b)
            print("el resultado de la suma es", resultado)
        case "restar":
            resultado = restar(a, b)
            print("el resultado de la resta es", resultado)
        case "multiplicar":
            resultado = multiplicar(a, b)
            print("el resultado de la multiplicacion es", resultado)
        case "dividir":
            resultado = dividir(a, b)
            print("el resultado de la division es",resultado)
        case _:
            print("resultado no valido.")
             
while True:
    a = int(input("ingrese el numero 1: "))
    b = int(input("ingrese el numero 2: "))
    operacion = input("ingrese la operacion a realizar ")
    calculadora(operacion)
 

