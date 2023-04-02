
def calcIMC(peso, altura):
    alt2 = altura**2
    imc = peso/alt2
    print("su IMC es: " + str(imc))

    if num == 1:
        if imc < 20:
            print("BAJO PESO")

        if imc >= 20 and imc <= 24.9:
            print("NORMAL")

        if imc >= 25 and imc <= 29.9:
            print("OBESIDAD LEVE")

        if imc >= 30 and imc <= 40:
            print("OBESIDAD SEVERA")
        
        if imc > 40:
            print("OBESIDAD MUY SEVERA")
    
    if num == 2:
        if imc < 20:
            print("BAJO PESO")
        if imc >= 20 and imc <= 23.9:
            print("NORMAL")

        if imc >= 24 and imc <= 28.9:
            print("OBESIDAD LEVE")

        if imc >= 29 and imc <= 37:
            print("OBESIDAD SEVERA")

        if imc > 37:
            print("OBESIDAD MUY SEVERA") 
    


print("CALCULAR IMC")
print("Ingrese su sexo")
num = int(input("1. Masculino 2. Femenino\n"))

if num == 1:
    peso = float(input("Ingrese su peso\n"))
    altura = float(input("Ingrese su altura en metros\n"))
    calcIMC(peso, altura)
else:
    if num == 2:
        peso = float(input("Ingrese su peso\n"))
        altura = float(input("Ingrese su altura en metros\n"))
        calcIMC(peso, altura)
    else:
        print("el numero ingresado es incorrecto")






