print("Ejercicio 10")
print("Introducir una cadena de caracteres e indicar si es un palíndromo.")
print("Una palabra palíndroma es aquella que se lee igual adelante que atrás.")
cadena=input("Ingrese la cadena: ")
palin=cadena[::-1]
if cadena==palin:
    print("La cadena que ingreso es un palindromo.")
else:
    print(f"La cadena que ingreso no es un palindromo: {palin}")