import math
print("Hola Buen dia. Vamos a calcular la hipotenusa de un triangulo rectangulo\nIngresando 2 catetos.")
cateto1=int(input("Ingrese el cateto 1: "))
cateto2=int(input("Ingrese el cateto 2: "))
hipotenusa= math.sqrt((cateto1*cateto1)+(cateto2*cateto2))
print(f"La hipotenusa es: {hipotenusa} ")
input()
