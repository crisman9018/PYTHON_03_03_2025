import csv
respuestas = {}

# Leer un CSV con encabezados
with open("preguntas.csv" , "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        respuestas[fila["preguntas"]] = fila["respuestas"]
        # Imprime cada fila como un diccionario
        
def generar_respuesta(pregunta):
    if pregunta in respuestas:
        return respuestas[pregunta]
    else:
        return "no entiendo tu pregunta"
    
print("Hola soy un chatbot en que puedo ayudarte\n")
while True:
    prompt = input("ingresa tu pregunta\n")
    if prompt == "salir":
        break
    respuesta = generar_respuesta(prompt)
    print(respuesta)