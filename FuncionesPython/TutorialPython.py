#Funciones
""" def mensaje():  #declaracion de la funcion

    print("Estamos aprendiendo Python")
    print("Estamos aprendiendo Instrucciones Básicas")
    print("Poco a poco iremos avanzando")

mensaje() #Llamado de la funcion

print("Ejecutando código fuera de la funcion")
mensaje() """

""" def suma(num1, num2):

    resultado=num1+num2
    return resultado
almacena_resultado=suma(5, 8) #Se declara una variable para guardar el resultado, para luego imprimirlo
print(almacena_resultado) """

#Listas
""" miLista=["Maria", "Pepe", "Marta", "Antonio"] #La posicion empieza en 0
miLista.append("Sandra") #Esto es para agregar elementos a la lista, siempre se agrega al final de la lista
miLista.insert(2,"Sandra") #Asi se agrega en una posicion expecifica
miLista.extend(["Sandra", "Ana", "Lucia"])#Para agregar varios elementos a la lista
miLista.remove("Ana") #Para eliminar elementos
miLista.pop() #Para eliminar el ultimo elemento de una lista
print(miLista[2]) #Entre corchetes va el valor a imprimir, segun la posicion : es para impirmir todos los parametros
print(miLista[0:3]) #Esto es acceder a una porcion, donde empieza en 0 y va hasta 3, es coger las 3 primeros elementos dejando excluido el 3
print(miLista[1:]) #Desde la posicion 2 hasta el final
print(miLista.index("Antonio"))#Para saber el indice(posicion) de un elemento
print("pepe" in miLista)#Comprobar si un elemento se encuentra o no en una lista """

""" miLista2=["Sandra", "Lucia"]
#Si queremos unir las dos listas, hay que crear una tercera lista
miLista3=miLista+miLista2
print(miLista3)

#El operador *(multiplicacion) lo que hace es repetir listas
miLista=["Maria", "Pepe", "Marta", "Antonio"] * 3 #Lo que hace es repetir 3 veces la lista """

#Tuplas: las tuplas es igual que una lista pero no podemos añadir elementos, ni borrar, ni mover elementos, no usa (append, remove, extend)
#Una tupla se ejecuta mas rapido que una lista, ocupa menos espacio y da mayor rendimiento
""" mitupla=("Juan", 13,1,1995) #Sintaxis
print(mitupla[2])#Para acceder a un elemento con posicion 2
miLista=list(mitupla)#Para coonvertir una tupla en una lista
print(miLista) #Se distingue por los corchetes[] y la tupla parentesis()
miLista=["Juan", 13,1,1995]#Creamos la lista para convertirla en tupla
mitupla=tuple(miLista)#Convertir una lista en tupla
print("Juan" in mitupla) #Para saber si esta el elementos
print(mitupla.count(13))#Para averiguar cuantas veces se encuentra un elemento 13
print(len(mitupla))#Para averiguar la longitud de una tupla, cuantos elementos hay
mitupla=("Juan",)#Tupla unitaria, siempre tiene que llevar la , para saber que es una tupla unitaria """
#Tambien se puede crear tuplas sin parentesis, se conoce como empaquetado de tupla
#Para desempaquetar la tupla se asignas unas variables, separados por comas
""" mitupla=("Juan", 13,1,1995)
nombre, dia, mes, agno = mitupla #Cada una de las tuplas por orden de variables asignadas
print(nombre)
print(dia)
print(mes)
print(agno) """