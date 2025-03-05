
# Imprimir el diccionario
respuestas = {
    "hola como estas" : "muy bien en que puedo ayudarte",
    "donde se encuentran ubicados" : "en la carrera 29 #50-20",
    "que cursos tienes disponible" : "tenemos bootcamps de programacion y analisis de datos",
    "cuando inician el curso" : "cada primmera semana al mes"
}

def generar_respuesta(pregunta):
    if pregunta in respuestas:
        return respuestas[pregunta]
    else:
        return "no entiendo tu pregunta"
    
print("hola soy un chatboy en que puedo ayudarte\n")
while True:
    prompt = input("ingresa tu pregunta\n")
    if prompt == "salir":
        break
    respuesta = generar_respuesta(prompt)
    print(respuesta)