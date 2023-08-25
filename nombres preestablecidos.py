"""1 Cree un vector con 5 nombres preestablecidos por el programador, mostrar en pantalla 
el nombre, posición que ocupa dentro del vector y posición que se mostraría comúnmente al usuario, 
utilizar un print por cada requerimiento a mostrar (tres en total)"""

#Declarando vector

x = ["Maria","Jose","Miguel","Jesus","Karla"] #Vector preestablecido

#Declarando iterador

i = 0
j = 0

print("Desarrollo de programa")

print("Impresion de información")

while i < len(x):
    print("El dato almacenado es: ",x[i])
    print("La posicion que el dato ocupa es: ", i)
    print("La posicion que el usuario visualiza es: {}\n".format(i+1))
    i += 1




