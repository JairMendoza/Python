import os  
menu=''
while menu.upper()!='X':
    os.system("cls")
    print("1.Informacion")
    print("2.Temas de control")
    print("3.terminal")
    print("Seleccione una opcion: ")
    menu=input(print("Para terminar precione 'X'"))
    if menu=='1':
        print("Hola.")
        input()
    elif menu=='2':
        print("como.")
        input()
    elif menu=='3':
        print("estas?.")
        input()
    elif menu.upper()=='X':
        break
    else:
        print("Opcion no valida.")
        input()
    