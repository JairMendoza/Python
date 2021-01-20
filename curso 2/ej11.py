print("Vamos a ingresar 2 numeros para saber la distancia que hay de uno a otro.")
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
if num1>num2:
    diferencia=num1-num2
else:
    diferencia=num2-num1
print(f"La diferencia es: {diferencia}")
input()