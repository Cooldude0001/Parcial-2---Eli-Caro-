# Programa que determine si en una lista no existen elementos repetidos 

# Listas de ejemplo
lista_1 = [] # Ejemplo de lista vacia
lista_2 = ["a", "a", "b", "c"] # Ejemplo de lista con elementos repetidos
lista_3 = ["a", "e", "i", "o"] # Ejemplo de lista con elementos sin repetir

def encontrar_repeticiones (nombre_lista):
    if len (nombre_lista) == 0:
        # Aqui se verifica que la lista suministrada tenga algun elemento
        return print (f"La lista que suministro se encuentra vacia")
    
    else:
        # la variable "comparador" representa los indices de la lista suministrada
        comparador = 1
        elementos_lista = nombre_lista [comparador]

        for cada_elemento in nombre_lista:
              
            if cada_elemento == elementos_lista:
                # En caso de que encuentre un elemento repetido va devolver la siguiente respuesta
                return print ("La lista que suministro contiene elementos repetidos")
            else:
                # Si la lista no contiene elementos repetidos va devolver la siguiente respuesta
                comparador += 1
                return print ("La lista que suministro no contiene elementos repetidos")


encontrar_repeticiones (lista_2)
