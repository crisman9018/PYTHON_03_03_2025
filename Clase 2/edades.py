
edad = int(input("ingresa la edad "))

def calculoedad(edad):
    if edad >=18 and edad < 60:
        print("es mayor de edad")
    elif edad >= 60:
        print("es adulto mayor")
    else:
        print("es menor de edad")
calculoedad(edad)

# Funciones Anonimas (Lambda)

suma = lambda x, y: x + y

resultado = suma (4, 7)
print(resultado)   # imprime 11