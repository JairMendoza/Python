print("Vamos a comprobar si un caracter esta dentro de una cadena.")
cad=input("Ingrese una cadena: ")
cad1=''
while len (cad1)!=1:
    cad1=input("Ingrese un caracter para comprobar si esta dentro de la cadena: ")
cont=cad.count(cad1)
print(f"El caracter que ingreso esta {cont} veces en la cadena.")