print("Vamos a ingresar una cadena caracter por caracter para luego invertirla.")
print("Para terminar precione 0")
cadena=""
car=""
while car!='0':
    car=""
    while len(car)!=1:
        car=input("Ingrese un caracter: ")
    if car!='0':
        cadena=cadena+car
inver=cadena[:: - 1 ]
print(f"La cadena que ingreso inver tida es: {inver}")