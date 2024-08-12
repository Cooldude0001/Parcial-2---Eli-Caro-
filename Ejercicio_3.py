# Desarrollar un programa que dadas dos listas determine que elementos
# tiene la primera lista que no tiene la segunda

# Listas utilizadas en el ejercicio
# Para fines practicos ambas listas van a tener el mismo numero de elementos
Lista_1 = ["a", "b", "c", "d", "f", "g"] 
Lista_2 = ["a", "b", "c", "e", "e", "g"] 

# Funcion para determinar elementos unicos de la primera lista
def Unique_Founder (nombre_lista_1, nombre_lista_2):
    if len (nombre_lista_1) == 0 or len (nombre_lista_1) == 0:
        return print ("No proporcione listas vacias")
    
    # Variables para comparar los elementos a traves de sus indices
    indice = 0
    almacemiento = [] # Aqui se guardan los elementos unicos de lista 1

    for todo_elemento in nombre_lista_1:
        # Compara todos los 
        comprobacion = (nombre_lista_1 [indice] == nombre_lista_2 [indice])

        if comprobacion == False:
            # Cuando se encuentre un elemento unico se guarda ese elemento en la lista almacenamiento
            almacemiento.append (nombre_lista_1 [indice])

        indice += 1   
    return print (f"El (Los) elemento(s) unico(s) de la lista 1 es(son): {almacemiento}")
             
Unique_Founder (Lista_2, Lista_1)
