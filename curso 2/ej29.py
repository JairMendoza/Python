print("Ingrese dos numeros y el programa imprimira los numeros pares que halla entre ellos.")
num1=int(input("Ingrese el Primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
par=0
if num1>num2:
    par=num1
    while par!=num2:
        if (par-1)%2==0:
            if par-1==num2:
                break
            print(par-1)
        par=par-1
if num2>num1:
    par=num2
    while par!=num1:
        if (par-1)%2==0:
            if par-1==num1:
                break
            print(par-1)
        par=par-1