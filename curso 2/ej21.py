print("Escribir un programa que lea un año indicar si es bisiesto.")
print("Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.")
anio=int(input("Ingrese un año: "))
ban=0
if anio%4==0:
    if anio%100==0:
        if anio%400==0:
            print("Es un año bisiesto.")
            ban=1
        else:
            print("No es un año bisiesto.")
            ban=1
    if anio%4==0 and ban==0:
        print("Es un año bisiesto.")
        ban=1
elif ban==0:
    print("No es un año bisiesto.")
input()