"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    datos = open("files/input/data.csv","r").readlines()
    datos = [d.split("\t") for d in datos]
    datos = [[d[1]] + [d[3]] for d in datos]
    #print(datos)
    suma = {}
    for lista in datos:
        #print(lista)
        lista = [tuple(lista)]
        #print(lista)
        for key, value in lista:
            value = value.split(",")
            for v in value:
                if v in suma:
                    suma[v] += int(key)
                else:
                    suma[v] = int(key)
    return(dict(sorted(suma.items())))

if __name__ == "__main__":
    pregunta_11()