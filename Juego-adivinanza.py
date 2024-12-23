

import random


numero_secreto = random.randint(1,100)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("bienvenido al juego de adivinar")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("¡game over!")
        break

    entrada = input("Introduce un numero del 1 al 99: ") # TODO: convertir a numero 
    numero = int(entrada)

    if numero == numero_secreto:
        print("Felicitaciones has adivinado el numero secreto")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero es mayor al ingresado")
    else:
        print("El numero es menor al ingresado")
    
    cant_intentos += 1

    