import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cuestionario Algoritmos Genéticos")
ventana.geometry("900x800")
ventana.config(bg="#f0e6ff")

# Lista de preguntas, opciones y respuesta correcta
preguntas = [
    {
        "pregunta": "¿Qué características de la evolución biológica inspiran el funcionamiento de los algoritmos genéticos?",
        "opciones": [
            "A) La fotosíntesis de las plantas",
            "B) La selección natural y la adaptación de las especies",
            "C) El crecimiento celular",
            "D) La mutación de virus en organismos"
        ],
        "respuesta_correcta": "B) La selección natural y la adaptación de las especies"
    },
    {
        "pregunta": "¿Cuál es el propósito principal de utilizar operadores como la selección, el cruzamiento y la mutación dentro de un algoritmo genético?",
        "opciones": [
            "A) Hace que el programa consuma menos memoria",
            "B) Generar nuevas soluciones y mejorar las existentes de manera progresiva",
            "C) Aumentar el número de generaciones sin modificar los resultados",
            "D) Eliminar individuos que no cumplan con los objetivos iniciales"
        ],
        "respuesta_correcta": "B) Generar nuevas soluciones y mejorar las existentes de manera progresiva"
    },
    {
        "pregunta": "¿En qué tipo de problemas o áreas se aplican comúnmente los algoritmos genéticos?",
        "opciones": [
            "A) Solo en videojuegos y simulaciones",
            "B) En optimizaciones de rutas, diseño de redes y toma de decisiones complejas",
            "C) Únicamente en biología computacional",
            "D) En cualquier problema que no requiera análisis matemático"
        ],
        "respuesta_correcta": "B) En optimizaciones de rutas, diseño de redes y toma de decisiones complejas"
    },
    {
        "pregunta": "¿Qué ventaja ofrecen los algoritmos genéticos frente a los métodos tradicionales de optimización?",
        "opciones": [
            "A) Siempre encuentra la solución perfecta en poco tiempo",
            "B) No necesita una función de evaluación para operar",
            "C) Puede explorar múltiples soluciones y adaptarse a distintos tipos de problemas",
            "D) Requiere menos pasos que cualquier otro algoritmo"
        ],
        "respuesta_correcta": "C) Puede explorar múltiples soluciones y adaptarse a distintos tipos de problemas"
    },
    {
        "pregunta": "¿Cuál es el propósito fundamental de los algoritmos genéticos (AGs) según su descripción en la fuente?",
        "opciones": [
            "A) La creación de bases de datos estructuradas",
            "B) La simulación de sistemas físicos deterministas",
            "C) Una técnica de optimización y búsqueda para resolver problemas complejos",
            "D) El análisis estadístico de grandes conjuntos de datos"
        ],
        "respuesta_correcta": "C) Una técnica de optimización y búsqueda para resolver problemas complejos"
    },
    {
        "pregunta": "¿Qué fenómeno natural sirve de inspiración para las técnicas de los algoritmos genéticos?",
        "opciones": [
            "A) El principio de inercia",
            "B) La evolución biológica",
            "C) La gravedad y sus efectos",
            "D) Los ciclos químicos"
        ],
        "respuesta_correcta": "B) La evolución biológica"
    },
    {
        "pregunta": "¿Mediante qué mecanismo principal funcionan los algoritmos genéticos?",
        "opciones": [
            "A) Mediante la aplicación de técnicas de regresión múltiple",
            "B) Mediante la resolución directa de ecuaciones diferenciales",
            "C) Simulando la selección natural",
            "D) Aplicando el método de Montecarlo"
        ],
        "respuesta_correcta": "C) Simulando la selección natural"
    },
    {
        "pregunta": "¿Cuál de las siguientes opciones nombra uno de los tres procesos fundamentales (operadores) que permiten la evolución iterativa de la población de soluciones?",
        "opciones": [
            "A) Cuantificación",
            "B) Normalización",
            "C) El cruce",
            "D) La inicialización"
        ],
        "respuesta_correcta": "C) El cruce"
    },
    {
        "pregunta": "¿El proceso de evolución en los algoritmos genéticos ocurre de qué manera?",
        "opciones": [
            "A) Estática e instantánea",
            "B) Lineal y constante",
            "C) Iterativa a lo largo de generaciones",
            "D) Puramente aleatoria sin retroalimentación"
        ],
        "respuesta_correcta": "C) Iterativa a lo largo de generaciones"
    },
    {
        "pregunta": "¿Cuál es el objetivo final de la evolución de la población a lo largo de las generaciones en un algoritmo genético?",
        "opciones": [
            "A) Un conjunto de soluciones dispersas",
            "B) La solución más compleja teóricamente",
            "C) Una solución óptima o casi óptima",
            "D) El punto de partida"
        ],
        "respuesta_correcta": "C) Una solución óptima o casi óptima"
    }
]

# Variables globales
respuestas = []
indice = 0
puntaje_correctas = 0
puntaje_incorrectas = 0
respondido = False

# Etiqueta de título
titulo = tk.Label(ventana, text="¡Bienvenido al cuestionario sobre Algoritmos Genéticos!",
                  font=("Comic Sans MS", 16, "bold"), bg="#f0e6ff", fg="#6a1b9a")
titulo.pack(pady=10)

# Contador de preguntas
contador = tk.Label(ventana, text="", font=("Arial", 11), bg="#f0e6ff", fg="#555")
contador.pack(pady=5)

# Etiqueta de pregunta
etiqueta_pregunta = tk.Label(ventana, text="", font=("Arial", 13, "bold"), bg="#f0e6ff", fg="#333", wraplength=800, justify="left")
etiqueta_pregunta.pack(pady=10)

# Variable para guardar selección del usuario
respuesta_var = tk.StringVar(value=None)

# Etiqueta de resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 11), fg="#7b1fa2", bg="#f0e6ff")
etiqueta_resultado.pack(pady=5)

# Lista de botones de opción
botones_opcion = []

# Reiniciar cuestionario
def reiniciar_cuestionario():
    global indice, puntaje_correctas, puntaje_incorrectas, respuestas, respondido
    indice = 0
    puntaje_correctas = 0
    puntaje_incorrectas = 0
    respuestas = []
    respondido = False
    
    # Mostrar nuevamente los elementos
    for boton in botones_opcion:
        boton.pack(pady=5, anchor="w", padx=50)
    frame_botones.pack(pady=10)
    boton_reiniciar.pack_forget()
    
    mostrar_pregunta()

# Mostrar una pregunta
def mostrar_pregunta():
    global respondido
    respondido = False
    contador.config(text=f"Pregunta {indice + 1} de {len(preguntas)}")
    etiqueta_pregunta.config(text=preguntas[indice]["pregunta"])
    respuesta_var.set(None)
    etiqueta_resultado.config(text="")
    for i, opcion in enumerate(preguntas[indice]["opciones"]):
        botones_opcion[i].config(text=opcion, value=opcion, state="normal")

# Validar respuesta
def validar_respuesta():
    global puntaje_correctas, puntaje_incorrectas, respondido

    if respondido:
        etiqueta_resultado.config(text="Ya respondiste esta pregunta", fg="#cc0000")
        return

    seleccion = respuesta_var.get()
    if not seleccion or seleccion == "None":
        etiqueta_resultado.config(text="Por favor selecciona una opción", fg="#cc0000")
        return

    correcta = preguntas[indice]["respuesta_correcta"]
    if seleccion == correcta:
        etiqueta_resultado.config(text="✓ ¡Correcto!", fg="#4caf50")
        puntaje_correctas += 1
    else:
        etiqueta_resultado.config(text=f"✗ Incorrecto. La respuesta correcta era: {correcta}", fg="#f44336")
        puntaje_incorrectas += 1

    respuestas.append(seleccion)
    respondido = True

    for boton in botones_opcion:
        boton.config(state="disabled")

# Avanzar a la siguiente pregunta
def siguiente_pregunta():
    global indice, respondido
    if not respondido:
        etiqueta_resultado.config(text="Primero responde la pregunta antes de continuar ⚠", fg="#ff9800")
        return

    indice += 1
    if indice < len(preguntas):
        mostrar_pregunta()
    else:
        mostrar_resultado()

# Mostrar botones de opción
for i in range(4):
    boton = tk.Radiobutton(
        ventana, text="", variable=respuesta_var,
        font=("Arial", 12), bg="#f0e6ff", fg="#333",
        activebackground="#e1bee7", selectcolor="#ffffff",
        anchor="w", justify="left", wraplength=800, width=100
    )
    boton.pack(pady=5, anchor="w", padx=50)
    botones_opcion.append(boton)

# Botones de acción
frame_botones = tk.Frame(ventana, bg="#f0e6ff")
frame_botones.pack(pady=10)

boton_validar = tk.Button(frame_botones, text="Validar respuesta ✅", command=validar_respuesta,
                          bg="#8e24aa", fg="white", font=("Arial", 11, "bold"), relief="raised",
                          padx=10, pady=5)
boton_validar.grid(row=0, column=0, padx=10)

boton_siguiente = tk.Button(frame_botones, text="Siguiente ➡", command=siguiente_pregunta,
                            bg="#ab47bc", fg="white", font=("Arial", 11, "bold"),
                            relief="raised", padx=10, pady=5)
boton_siguiente.grid(row=0, column=1, padx=10)

# Botón de reinicio (inicialmente oculto)
boton_reiniciar = tk.Button(ventana, text="🔄 Volver a hacer el cuestionario", command=reiniciar_cuestionario,
                            bg="#673ab7", fg="white", font=("Arial", 12, "bold"),
                            relief="raised", padx=15, pady=8)

# Mostrar resultado final
def mostrar_resultado():
    etiqueta_pregunta.config(text="¡Gracias por completar el cuestionario! 💫")
    contador.config(text="")
    for boton in botones_opcion:
        boton.pack_forget()
    frame_botones.pack_forget()

    texto_final = "\n".join([f"{i+1}. {r}" for i, r in enumerate(respuestas)])
    resumen = (f"Tus respuestas fueron:\n\n{texto_final}\n\n"
               f"✅ Correctas: {puntaje_correctas}\n"
               f"❌ Incorrectas: {puntaje_incorrectas}\n"
               f"Puntaje final: {puntaje_correctas}/{len(preguntas)} 🎯")

    etiqueta_resultado.config(text=resumen, fg="#6a1b9a", wraplength=800, justify="left")
    
    # Mostrar botón de reinicio
    boton_reiniciar.pack(pady=20)

# Iniciar la primera pregunta
mostrar_pregunta()

# Ejecutar loop principal
ventana.mainloop()
