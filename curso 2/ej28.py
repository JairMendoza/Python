print("Vamos a ingresar los numeros que guste y los sumaremos\nPara terminar precione 0")
num=10
cont=0
suma=0
while num!=0:
    num=int(input("Ingrese numero: "))
    if num ==0:
        break
    else: 
        cont=cont+1
        suma=suma+num
print(f"La suma de los numeros que ingreso es: {suma}.\nY la media de todos los numeros introducidos es {suma/cont}.")