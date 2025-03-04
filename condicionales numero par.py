#funcion que al ingresar un numero me diga si es par o impar

numero = int(input("ingrese un numero"))

def numeropar(numero):
    if numero % 2 == 0:
        print(f"el numero {numero} es par")
    else:
        print(f"el numero {numero} es impar")   
numeropar(numero)