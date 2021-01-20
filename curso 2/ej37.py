import random
import math
print("Ejercicio 1")
print("Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)")
print("y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.")
lista=[]
for num in range(10):
    lista.append(random.randrange(10))
for i in range(10):
    print(lista[i],lista[i]*lista[i],pow(lista[i],3))
print(lista)