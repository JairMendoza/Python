print("Vamos a ingresar 3 numeros para ordenarlos de mayor a menor.")
num1=int(input("Ingrese el numero 1: "))
num2=int(input("Ingrese el numero 2: "))
num3=int(input("Ingrese el numero 3: "))
if num1<num2 and num1<num3:
    if num2<num3:
        print(f"{num1}, {num2}, {num3}")
    if num3<num2:
        print(f"{num1}, {num3}, {num2}")
if num2<num1 and num2<num3:
    if num1<num3:
        print(f"{num2}, {num1}, {num3}")
    if num3<num1:
        print(f"{num2}, {num3}, {num1}")
if num3<num2 and num3<num1:
    if num2<num1:
        print(f"{num3}, {num2}, {num1}")
    if num1<num2:
        print(f"{num3}, {num1}, {num2}")
input()