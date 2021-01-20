print("Vamos a categorizar que tipo de trinagulo es segun sus medidas.")
print("Ingrese sus medidas:")
lado1=int(input("Ingrese el lado1: "))
lado2=int(input("Ingrese el lado2: "))
lado3=int(input("Ingrese el lado3: "))
ban=0
if lado1>lado2 and lado1>lado3:
    if lado1**2==lado2**2 +lado3**2:
        print("Es un triangulo rectangulo.")
        ban=1
if lado2>lado1 and lado2>lado3:
    if lado2**2==lado1**2 +lado3**2:
        print("Es un triangulo rectangulo.")
        ban=1
if lado3>lado2 and lado3>lado1:
    if lado3**2==lado2**2 +lado1**2:
        print("Es un triangulo rectangulo.")
        ban=1
if lado1== lado2 and lado3==lado2:
    print("Es un triangulo equilatero.")
    ban=1
if lado1==lado2 or lado1==lado3 or lado2==lado3:
    print("Es un triangulo isosceles.")
    ban=1
if ban==0:
    print("Es un triangulo escaleno.")
input()