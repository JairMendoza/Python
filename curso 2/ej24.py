print ("Vamos a ver cuanto tiene que pagar cada alumno.")
alumnos=int(input("Ingrese cuantos alumnos iran al viaje: "))
pago=0.0
if alumnos>99:
    pago=65*alumnos
if alumnos<100 and alumnos>49:
    pago=70*alumnos
if alumnos<50 and alumnos>29:
    pago=95*alumnos
if alumnos<30:
    pago=4000/alumnos
    print(f"EL pago que tendra que hacer cada alumno es: ${pago}")
    print("EL pago que se le debera hacer a la empresa es: $4000")
else:
    print(f"EL pago que tendra que hacer cada alumno es: {pago/alumnos}")   
    print(f"EL pago que se le debera hacer a la empresa es: {pago}")