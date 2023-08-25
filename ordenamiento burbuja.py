"""2 - Cree un vector con los siguientes valores: 66,20,80,38,11,35

- Mostrar el vector

- Utilizar el método de burbuja, para para ordenar las cantidades

- Modificar el algoritmo para que se ingresen valores hasta que el usuario decida detenerse, 
además validar que se hayan ingresado una cantidad mínima de 5 valores, 
mostrar un mensaje de advertencia al usuario si decide detenerse antes de cumplir esta norma 
y no detener la lectura

- Para mostrar el vector ordenado, preguntar al usuario si desea verlo de forma ascendente 
o descendente"""

#Declarando el vector

x = []

#Declarando el iterador

h = 0
i = 0
j = 1

# Declarando auxiliar

aux = 0

# Declarando controlador

contro = True

# Declarando variables

s = ""
n = ""
res = ""

a = ""
d = ""
res2 = ""

# Ingreso de datos

while contro == True:
    h += 1
    x.append (float(input("\nFavor ingresar el valor {}: ".format(h))))
    res = input(("\nSi: s \nNo: n \n¿Desea ingresar más valores?: ") )
    while res != "s" and res != "n":
        print("\nHa ingresado un valor invalido")
        res = input("\nSi: s \nNo: n \n¿Desea ingresar más valores?: ")
    print("\nRespuesta aceptada") 
    if res == "s":
        contro = True
        print("\nDe vuelta al ingreso")
    else:
        if h > 4:
            contro = False
            print("\nFin del ingreso de datos")
        else:
            print("\nLo sentimos, debe ingresar un minimo de 5 valores para terminar el ingreso")
    

print("\nImpresion del vector\n")

while i < len(x):
    print(x[i]) 
    i += 1



"""Inicia el ordenamiento por burbuja"""

#Ordenamiento burbuja con FOR

"""for i in range (len(x)): #Cuantas vueltas son necesarias para que el ordenamiento este completo. Posiblemente el vector ya este ordenado antes de recorrer todas las rondas
    for j in range (len(x)-1): #Encargado de hacer las comparaciones entre posiciones, para cada una de las rondas establecidas por el primer FOR
        if x[j] > x[j+1]: #Aqui comparo si la posicion actual es mayor a la posicion siguiente
            aux = x[j+1]
            x[j+1] = x[j]
            x[j] = aux"""

#En el for J recorrio 5 vueltas y despues el debug se pasó al for i
#Porque al recorrer una vez las 5 vueltas en for j, eso es una vuelta para el for i
# Es decir si recorre 5 vueltas en el for j y tiene que recorrer 6 vueltas en el for i
#En realidad el programa va a recorrer 30 vueltas

#Ordenamiento burbuja con WHILE

#Reinicio de iteradores

i = 0


while i < len(x):  #Cuantas vueltas son necesarias para que el ordenamiento este completo. Posiblemente el vector ya este ordenado antes de recorrer todas las rondas
    j = 0
    while j < (len(x)-1): #Encargado de hacer las comparaciones entre posiciones, para cada una de las rondas establecidas por el primer FOR
        if x[j] > x[j+1]: #Aqui comparo si la posicion actual es mayor a la posicion siguiente
            aux = x[j+1]
            x[j+1] = x[j]
            x[j] = aux
        j += 1
    i += 1

#En el while J recorrio 5 vueltas y despues el debug se pasó al while i
#Porque al recorrer una vez las 5 vueltas en while j, eso es una vuelta para el while i
# Es decir si recorre 5 vueltas en el while j y tiene que recorrer 6 vueltas en el while i
#En realidad el programa va a recorrer 30 vueltas

# Reiniciar el iterador

i = 0

while res2 != "a" and res2 != "d":
    print("\nHa ingresado un valor invalido")
    res2 = input("\nAscendente: a \nDescendente: d \n¿Como queire ver el vector?: ")
print("\nRespuesta aceptada") 
if res2 == "a":
    while i < len(x):
        print(x[i]) 
        i += 1
else:
    i = len(x)-1
    while i >= 0:
        print(x[i]) 
        i = i - 1 





