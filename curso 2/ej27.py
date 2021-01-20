import random
import os
intentos=10
numero=random.randrange(100)
num=200
acierto=0
while num!=numero:
    os.system("cls")
    print(f"Vamos a generar  un numero aleatorio entre 0 y 100 el cual\ntu deberas atinar\ntienes {intentos} intentos.")
    num=int(input("Ingrese el numero: "))
    if num==numero:
        acierto=1
        break
    elif num>numero:
        print("El numero que ingreso es mayor al que hay que adivinar.")
        intentos=intentos-1
    else:
        print("El numero que ingreso es menor al que hay que adivinar.")
        intentos=intentos-1
    if intentos==0:
        acierto=2
        break
    input()
if acierto==1:
    print(f"Atinaste al numero random!\n lo hiciste en {10-intentos} intentos")
if acierto==2:
    print(f"No haz logrado atinar al numero rando :c\n el numero era: {numero}")
input()
