import random

def contar_vocales(palabra: str) -> list:
    """Retorna una lista de vocales (incluidas acentuadas) encontradas en la palabra."""
    vocales_permitidas = 'aeiouáéíóú'
    return [letra for letra in palabra.lower() if letra in vocales_permitidas]

def main():
    palabras = [
        "Aceituna", "Murciélago", "Educación", "Aeropuerto", "Otorrinolaringólogo",
        "Euforia", "Aceite", "Paleontólogo", "Arquitectura", "Hipopótamo"
    ]

    palabra = random.choice(palabras)
    vocales = contar_vocales(palabra)
    vocales_unicas = sorted(set(vocales), key=vocales.index)

    print("Análisis de Vocales en una Palabra Aleatoria")
    print(f" Palabra seleccionada : {palabra}")
    print(f" Vocales encontradas   : {', '.join(vocales)}")
    print(f" Vocales únicas        : {', '.join(vocales_unicas)}")
    print(f" Total de vocales      : {len(vocales)}")