print("Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d.") 
print("El que está detrás viaja a una velocidad mayor.")
print("Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h)") 
print("y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.")
Velocidad1=float(input("Ingrese la velocidad v1: "))
Velocidad2=float(input("Ingrese la velocidad v2: "))
distancia=float(input("Ingrese la distancia(km): "))
if Velocidad1>Velocidad2:
    tiempo=distancia/(Velocidad1-Velocidad2)
else:
    tiempo=distancia/(Velocidad2-Velocidad1)
tiempo=tiempo*60
print(f"El tiempo que tardara el coche de detras en alcanzar al de delante es: {tiempo} minutos.")
input()