# MODERADOR DE REDES SOCIALES

# 1. NUESTROS DATOS (Comentarios en una publicación)
comentarios_nuevos = [
    "Qué bonito video",
    "Eres muy tonto",
    "Excelente contenido",
    "Odio esta publicación",
    "Muy buen trabajo",
    "Qué buena publicación",
    "Eres un acomplejado",
    "Me encantó el contenido",
    "Qué comentario tan tóxico",
    "Que feo te vezz,dedicate a otra cosa,tonto"
]

# 2. NUESTRO MODELO (Palabras prohibidas por la comunidad)

palabras_toxicas = [
    "tonto",
    "odio",
    "idiota",
    "estúpido",
    "feo",
    "toxico"
]

def modelo_ia_moderador(comentario):
    comentario_minuscula = comentario.lower()

    # El modelo busca si hay lenguaje ofensivo
    for palabra in palabras_toxicas:
        if palabra in comentario_minuscula:
            return "BLOQUEADO (Tóxico)"  # Predicción 1

    return "APROBADO (Seguro)"  # Predicción 2

# 3. EVALUACIÓN Y PREDICCIÓN

print("--- MODERADOR DE REDES SOCIALES ---")

for i, comentario in enumerate(comentarios_nuevos, 1):
    prediccion = modelo_ia_moderador(comentario)
    print(f"Comentario {i}: '{comentario}' -> ESTADO: {prediccion}")
