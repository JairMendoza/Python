print("Vamos a ingresar su nombre con todos sus apellidos y le mostrare sus iniciales.")
nombre=str(input("Ingrese su nombre completo: "))
indice=0
while indice < len(nombre):
    punt=nombre[indice]
    if indice==0:
        inicial=punt
    if punt==' ':
        inicial=inicial+ nombre[indice+1]
    indice+=1
print(inicial)
input()
