print("La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva,")
print("la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto,")
print("ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor")
print("por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,")
print("se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2.")
print("Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2.")
print("Realice un algoritmo para determinar la ganancia obtenida.")
precio=int(input("Ingresa el precio de uva por kilo: "))
kilos=int(input("Ingresa cuantos kilos has vendido: "))
tipo=input("Ingrese el tipo de uva(A/B):")
tamaño=int(input("Ingrese el tamaño de la uva(1/2)"))
ganancia=0.0
suma=0
if tipo=='A' or tipo=='a':
    if tamaño==1:
        suma=.20
    if tamaño==2:
        suma==.30
    ganancia=(precio*kilos)+(suma*kilos)
if tipo=='B' or tipo=='b':
    if tamaño==1:
        suma=-.30
    if tamaño==2:
        suma=-.50
    ganancia=(precio*kilos)+(suma*kilos)
print(ganancia)
input()