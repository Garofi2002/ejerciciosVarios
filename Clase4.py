#El usuario escoge que opcion desea usar
opcion=int(input('Escriba una opcion\n'
                 '1.Sumar\n'
                 '2.Restar\n'
                 '3.Multiplicar\n'
                 '4.Dividir\n'))

if(opcion==1):#Verificar que se igual a 1
    print("Escogiste sumar")#Muestra la opcion que escogio
    #Permite que el usuario ingrese los 2 numeros
    num1 = int(input('Ingrese el primer numero'))
    num2 = int(input('Ingrese el segundo numero'))
    if(num1 <=0 or num2<=0):#Valida que los numeros no sean negativos ni 0
        print('Error: No se permite numero negativos ni 0')
    else:
        resultado=int(num1+num2)#realiza la operacion y guarda el resultado
        print(f'El resultado de la suma es: {resultado}')
elif(opcion==2):#Verificar que se igual a 2
    print("Escogiste Restar")#Muestra la opcion que escogio
    # Permite que el usuario ingrese los 2 numeros
    num1 = int(input('Ingrese el primer numero'))
    num2 = int(input('Ingrese el segundo numero'))
    if (num1 <= 0 or num2 <= 0):  # Valida que los numeros no sean negativos ni 0
        print('Error: No se permite numero negativos ni 0')
    else:
        resultado=int(num1-num2)#realiza la operacion y guarda el resultado
        print(f'El resultado de la suma es: {resultado}')
elif(opcion==3):#Verificar que se igual a 3
    print("Escogiste Multiplicar")#Muestra la opcion que escogio
    # Permite que el usuario ingrese los 2 numeros
    num1 = int(input('Ingrese el primer numero'))
    num2 = int(input('Ingrese el segundo numero'))
    if (num1 <= 0 or num2 <= 0):  # Valida que los numeros no sean negativos ni 0
        print('Error: No se permite numero negativos ni 0')
    else:
        resultado=int(num1*num2)#realiza la operacion y guarda el resultado
        print(f'El resultado de la suma es: {resultado}')
elif(opcion==4):#Verificar que se igual a 5
    print("Escogiste Dividir")#Muestra la opcion que escogio
    # Permite que el usuario ingrese los 2 numeros
    num1 = int(input('Ingrese el primer numero'))
    num2 = int(input('Ingrese el segundo numero'))
    if (num1 <= 0 or num2 <= 0):  # Valida que los numeros no sean negativos ni 0
        print('Error: No se permite numero negativos ni 0')
    else:
         resultado=int(num1/num2)#realiza la operacion y guarda el resultado
         print(f'El resultado de la suma es: {resultado}')
else:#Aqui cae si no es numero mencionado en la salida de consola
    print("Lo siento ese numero no esta en las opciones")