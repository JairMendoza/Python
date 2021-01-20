print("Ejercicio 7")
print("Pide una cadena y dos caracteres por teclado (valida que sea un carácter),")
print("sustituye la aparición del primer carácter en la cadena por el segundo carácter.")
cadena=input("Ingresa la cadena: ")
caracter1=""
caracter2=""
while len(caracter1)!= 1:
    caracter1=input("Ingrese un caracter: ")
while len(caracter2)!= 1:
    caracter2=input("Ingrese un 2do caracter: ")
print(cadena.replace(caracter1,caracter2))
