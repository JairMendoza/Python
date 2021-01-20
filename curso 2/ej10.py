cal1=float(input("Ingrese su primera calificacion parcial."))
cal2=float(input("Ingrese su segunda calificacion parcial."))
cal3=float(input("Ingrese su tercera calificacion parcial."))
porcentaje1=(cal1+cal2+cal3)/(3)*.55
examen=float(input("Ingrese su calificacion de su examen final."))
porcentaje2=examen*.30
trabajo=float(input("Ingrese su calificacion de su tranajo final.")) 
porcentaje3=trabajo*.15
final=porcentaje1+porcentaje2+porcentaje3
print(f"Su calificacion final es: {final}")
input()