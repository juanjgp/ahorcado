from random import *
import sys

# Inicio del juego
print("¡Bienvenido al juego del ahorcado!")
print("----------------------------------")

vidas = 6
aciertos = []
fallos = []
lista_palabras = ["cazador", "perro", "agujero", "ordenador", "lengua"]

# FUNCIONES
# Función elegir palabra al azar
def elegir_palabra_azar(lista):
    return choice(lista)

# Función mostrar guiones
def ocultar_palabra(palabra):
    return "-" * len(palabra)

# Función pedir letra al usuario
def pedir_letra(aciertos, fallos, palabra_oculta):
    mostrar_aciertos(aciertos)
    mostrar_fallos(fallos)
    print(palabra_oculta)
    letra_usuario = input("Introduce una letra: ")
    return letra_usuario

# Función validar letra
def validar_letra(letra, vidas, aciertos, fallos, palabra_oculta):
    while True:
        if len(letra) != 1:
            print("¡Fallo!. Debes introducir solo una letra. Pierdes una vida.")
            vidas -= 1
            mostrar_vidas(vidas)
            pierdes_juego(vidas)
            letra = pedir_letra(aciertos, fallos, palabra_oculta)
        elif not letra.isalpha():
            print("¡Fallo!. Debes introducir una letra, no un número o caracter extraño. Pierdes una vida.")
            vidas -= 1
            mostrar_vidas(vidas)
            pierdes_juego(vidas)
            letra = pedir_letra(aciertos, fallos, palabra_oculta)
        elif letra in aciertos or letra in fallos:
            print("¡Fallo!. Ya has dicho esa letra con anterioridad. Pierdes una vida.")
            vidas -= 1
            mostrar_vidas(vidas)
            pierdes_juego(vidas)
            letra = pedir_letra(aciertos, fallos, palabra_oculta)
        else:
            print("Letra correcta")
        return letra, vidas

# Función letra en palabra
def letra_en_palabra(letra, palabra, vidas, palabra_oculta):
    if letra in palabra:
        print("La letra se encuentra en la palabra.")
        aciertos.append(letra)
        mostrar_aciertos(aciertos)
        palabra_oculta = letra_acertada(letra, palabra, palabra_oculta)
        mostrar_palabra_oculta(palabra_oculta)
        
    else:
        print("La letra no se encuentra en la palabra.")
        print("Pierdes una vida.")
        fallos.append(letra)
        vidas -= 1
        mostrar_fallos(fallos)
        mostrar_vidas(vidas)
    return vidas, palabra_oculta

# Función cambiar guiones por letra acertada
def letra_acertada(letra, palabra, palabra_oculta):
    palabra_oculta_lista = list(palabra_oculta)

    for i, char in enumerate(palabra):
        # Solo escribir si coincide la letra Y en la oculta hay un guion
        if char == letra and palabra_oculta_lista[i] == "-":
            palabra_oculta_lista[i] = letra

    return "".join(palabra_oculta_lista)

# Función mostrar aciertos
def mostrar_aciertos(lista):
    print(f"Letras acertadas {lista}")

# Función mostrar fallos
def mostrar_fallos(lista):
    print(f"Letras falladas {lista}")

# Función mostrar vidas
def mostrar_vidas(vidas):
    print(f"Vidas restantes {vidas}")

# Función mostrar nueva palabra oculta
def mostrar_palabra_oculta(palabra_oculta):
    print(palabra_oculta)

# Función pierdes el juego si te quedas sin vidas
def pierdes_juego(vidas):
    if vidas == 0:
        print("¡Te has quedado sin vidas!. PIERDES EL JUEGO.")
        input("PRESIONA ENTER PARA FINALIZAR EL PROGRAMA.")
        sys.exit()

# Función ganas el juego si completas la palabra
def ganas_juego(palabra_oculta, palabra_elegida):
    if palabra_oculta == palabra_elegida:
        print(f"¡Has acertado la palabra! era {palabra_elegida}. GANAS EL JUEGO.")
        input("PRESIONA ENTER PARA FINALIZAR EL PROGRAMA.")
        sys.exit()

# PROGRAMA PRINCIPAL
palabra_elegida = elegir_palabra_azar(lista_palabras)
palabra_oculta = ocultar_palabra(palabra_elegida)

while vidas != 0:
    letra_usuario = pedir_letra(aciertos, fallos, palabra_oculta)
    letra_validada, vidas = validar_letra(letra_usuario, vidas, aciertos, fallos, palabra_oculta)
    vidas, palabra_oculta = letra_en_palabra(letra_validada, palabra_elegida, vidas, palabra_oculta)
    ganas_juego(palabra_oculta, palabra_elegida)

