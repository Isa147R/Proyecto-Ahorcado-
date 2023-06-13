import random

def obtener_palabra_aleatoria():
    palabras = ["python", "programacion", "computadora", "ahorcado", "juego"]
    return random.choice(palabras)

def mostrar_tablero(palabra, letras_adivinadas, intentos_restantes):
    print("Palabra:", end=" ")
    for letra in palabra:
        if letra in letras_adivinadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("\nIntentos restantes:", intentos_restantes)

def pedir_letra():
    letra = input("Ingresa una letra: ")
    return letra.lower()

def jugar_ahorcado():
    palabra = obtener_palabra_aleatoria()
    letras_adivinadas = []
    intentos_restantes = 6

    while True:
        mostrar_tablero(palabra, letras_adivinadas, intentos_restantes)

        if intentos_restantes == 0:
            print("\n¡Perdiste! La palabra era:", palabra)
            break

        letra = pedir_letra()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra not in palabra:
            intentos_restantes -= 1
            print("¡Letra incorrecta!")

        if all(letra in letras_adivinadas for letra in palabra):
            print("\n¡Felicidades! ¡Ganaste!")
            break

jugar_ahorcado()
