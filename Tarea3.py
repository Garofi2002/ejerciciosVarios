#Ejercicio numero 1

#variable que nos ayuda con el alto de rectangulo  y el usuario no permite ingresar la informacion
base=int(input('Ingrese la base del rectangulo:'))

#variable que nos ayuda con el alto de rectangulo  y el usuario no permite ingresar la informacion
alto=int(input('Ingrese la altura del rectangulo: '))

#El if compara que la base y la altura sean mayor de 0 y el or nos ayuda a saber si alguna de nuestras variables tiene un 0
if (base <= 0 or alto <=0 ):
    print("Error:Ingrese nuevamente los datos")#Cuando algun dato es igual a cero nos tira este print
else:
    area=base*alto#Aqui se realiza la operacion del area del rectangulo
    #Muestra el mensaje con el area del rectangulo
    print("El area del rectangulo es: "+ str(area))

#Ejercicio numero 2
#En esta parte se maneja las variables de las 3 notas y el prmedio
num1=int(input('Ingresa la primera nota: '))#Ingresa el valor de la primera nota
num2=int(input('Ingresa la segunda nota: '))#Ingresa el valor de la segunda nota
num3=int(input('Ingresa la tercera nota: '))#Ingresa el valor de la tercera nota
promedio=(num1+num2+num3)/3#Esta variable tiene la operacion del promedio

if (num1 < 0 or num2 < 0 or num3<0):#Aqui se compara que todas las variables sean de numeros positivos
    print('Error:Ingresaste algun valor en negativo')
elif (num1 <= 0 or num2 <= 0 or num3<=0):#Aqui se compara que todas las variables sean mayor a cero
    print('Las notas deben ser mayor que cero')
else:
    print('Su promedio fue de: ' + str(promedio))  # Se imprime el promedio

#Ejercicio numero 3
nota=int(input('Escriba la nota del curso: '))#variable de la nota ingresada por el usuario

if(nota < 0):#valida que la nota sea positiva
    print('Error:La nota fue negativa, pongala nueva')
elif(nota < 71):#valida que la nota sea menor de 71
    print('Lo siento reprobaste el curso')
elif(nota <= 71 or nota <= 90):#valida que la nota sea igual o mayor de 71 y menor de 90
    print('Felicidades aprobaste el curso')
else:#valida que la nota sea mayor de 91
    print('Aprobaste el curso, hiciste un excelente trabajo')

#Ejercicio numero 4
#variable donde el usuario pondra el numero entero
numero=int(input('Escriba un numero entero'))

if(numero == 0 ):#Compara si el numero es igual a creo
    print('El numero fue  igual a cero')
elif (numero < 0):#Compara que el numero es menor que cero, osea el numero es negativo
    print('El numero que ingreso fue negativo')
else:#Aqui si el numero es mayor a cero osea mayor a cero, osea el numero es positivo
    print('El numero que ingreso fue positivo')

#Ejercicio 5
#Variables donde el usuario coloco los 3 numero
primer=int(input('Ingrese el primer numero'))
segundo=int(input('Ingrese el segundo numero'))
tercero=int(input('Ingrese el tercero numero'))
#Se utilizaron las palabras claves max y min para encontrar el numero mayor y menor
mayor=max(primer,segundo,tercero)
menor=min(primer,segundo,tercero)

if(primer <= 0 or segundo <=0 or tercero<=0):#Compara si hay valores negativos o ceros
    print('Error:Uno de los numeros ingresados fueron 0 o en negativo')
else:
    #Imprime el numero mayor y el numero menos
    print('El numero mayor fue:'+str(mayor))
    print('El numero menor fue:' + str(menor))








