from datetime import datetime
print("Vamos a ingresar una fecha y te dire si es valida.")
while True:
    fecha_str = input('\n Ingrese fecha "dd/mm/aaaa"...: ')
    try:
        fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
    except ValueError:
        print("\n No ha ingresado una fecha correcta...")
    else:
        break