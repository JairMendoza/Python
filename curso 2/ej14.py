print("Vamos a intercambiar 2 numeros, y despues te mostrare la suma de esos 2 numeros.")
num1=int(input("Ingrese el numero 1: "))
num2=int(input("Ingrese el numero 2: "))
num3=num1
num1=num2
num2=num3
num3=num1+num2
print(f"El numero1 es: {num1} y el numero2 es: {num2} y la suma de esos dos numeros es: {num3}")
input()