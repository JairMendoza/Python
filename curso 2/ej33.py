print("Vamos a ingresar un texto para luego contar cuantas palabras tiene.")
tex=input("ingrese el texto: ")
cont=1
for palabras in tex:
    if palabras==" ":
        cont=cont+1
print(f"El texto tiene {cont} palabras.")