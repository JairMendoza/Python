print("Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.")
print("El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.")
print("Escribir un algoritmo que determine la hora de llegada a la ciudad B.")
segundos=int(input("Ingrese los segundos que tarda en llegar el ciclista: "))
hora1=int(input("Ingrese la hora a la que sale el ciclista de la ciudad(HH): "))
minuto1=int(input("Ingrese los minutos (MM): "))
segundo1=int(input("Ingrese los segundos (MM): "))
suma=(hora1*60)*60+(minuto1*60)+segundo1+segundos
minuto1=suma/60
hora1=minuto1/60
minuto1=(float(hora1)-int(hora1))*60
segundo1=(float(minuto1)-int(minuto1))*60
print(f"El ciclista llegara a las {int(hora1)}:{int(minuto1)}:{int(segundo1)}.")
input()