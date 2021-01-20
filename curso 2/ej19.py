print("Programa que lea una cadena por teclado y compruebe si hay una letra mayúscula.")
cadena=str(input("Ingrese una cadena a revizar: "))
indice=0
letras=""
while indice < len(cadena):
    letra=cadena[indice]
    if letra >='A' and letra <='Z':
        letras=letras+letra  
    indice+=1
if letras=="":
    print("Todas las letras son minusculas.")
else:
    print(f"Si hay letras mayusculas y son: {letras}")
input()