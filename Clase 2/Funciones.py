def saludar():
    print("Hola mundo")
    
saludar()

# Clase del 3-Marzo-2025 

def saludar(nombre):
    print(f"Hola {nombre}")
    
saludar("Jorge")

def saludar(nombre,apellido):
    print(f"Hola {nombre} {apellido}")
    
nombre = input("ingrese su nombre\n")
apellido = input("ingrese su apellido\n")
               
saludar(nombre,apellido)

def sumar(a, b):
    return a + b
resultado = sumar(5, 3)
print(resultado)          # imprime 8


def sumar(a, b):
    return a + b

a = float(input("ingrese el numero uno\n"))
b = int(input("ingrese el numero dos\n"))

resultado = sumar(a, b)

print(resultado)   



def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    return a / b

a = int(input("ingrese el numero uno\n"))
b = int(input("ingrese el numero dos\n"))

resultado1 = sumar(a, b)
print("el resultado de la suma es",resultado1)
resultado2 = restar(a, b)
print("el resultado de la resta es",resultado2)
resultado3 = multiplicar(a, b)
print("el resultado de la multiplicacion es",resultado3)
resultado4 = dividir(a, b)
print("el resultado de la division es",resultado4)
          