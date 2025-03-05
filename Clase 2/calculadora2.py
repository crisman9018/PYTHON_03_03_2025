def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calculadora(a, b, operacion):
    match operacion:
        case "suma":
            resultado = sumar(a, b)
            print("El resultado de la suma es", resultado)
        case "resta":
            resultado = restar(a, b)
            print("El resultado de la resta es", resultado)
        case "multiplica":
            resultado = multiplicar(a, b)
            print("El resultado de la multiplicación es", resultado)
        case "dividir":
            resultado = dividir(a, b)
            print("El resultado de la división es", resultado)
        case _:
            print("Operación no válida.")
            
while True:
    a = int(input("Ingrese el número 1: "))
    b = int(input("Ingrese el número 2: "))
    operacion = input("Ingrese la operación a realizar (suma, resta, multiplica, dividir) o 'salir' para terminar: ").lower()
    if operacion == "salir":
        break
    else:
        calculadora(a, b, operacion)