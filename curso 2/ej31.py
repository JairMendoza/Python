print("Vamos a comprobar si una cadena esta dentro de otra.")
cad=input("Ingrese una cadena: ")
cad1=input("Ingrese una cadena para comprobar si esta dentro de la otra: ")
if cad.find(cad1)==-1:
    print("La cadena no esta dentro de la primera cadena.")
    input()
else:
    print("La cadena esta dentro de la primera cadena.")
    input()