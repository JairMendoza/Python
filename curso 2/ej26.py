print(("Vamos a ingresar un numero y a calcular su factorial."))
numero=int(input("Ingrese el numero: "))
factorial=0
numero1=numero
while numero1!=1:
    factorial= numero*(numero1-1)
    numero=factorial
    numero1=numero1-1
print(f"El factorial del numero ingresado es: {factorial}")
input()