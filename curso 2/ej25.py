print("El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido.")
print("Lo anterior se muestra en la tabla:")
print("ZonaUbicaciónCosto/gramo")
print("1.-América del Norte 24.00 euros\n2.-América Central 20.00 euros\n3.-América del Sur 21.00 euros\n4.-Europa 10.00 euros\n5.-Asia 18.00 euros")
pago=0
zona=int(input("Ingrese la zona a la que va el paquete(1/2/3/4/5): "))
while zona<0 or zona>6:
    zona=int(input("Ingrese la zona a la que va el paquete(1/2/3/4/5): "))
peso=int(input("Ingrese el peso del paquete: "))
while peso<0 or peso>6:
    peso=int(input("ERROR. No se admiten paquetes mayores a 5 kg.\nIngrese el peso del paquete: "))
if zona==1:
    pago=24*peso
if zona==2:
    pago=20*peso
if zona==3:
    pago=21*peso
if zona==4:
    pago=10*peso
if zona==5:
    pago=18*peso
print(f"el costo del envio es: {pago} euros.")
input()