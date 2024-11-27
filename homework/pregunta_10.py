"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    datos = open("files/input/data.csv","r").readlines()
    datos = [d.split("\t") for d in datos]
    datos = [[d[0]] + d[-2:] for d in datos]
    datos = [(d[0], d[1].count(",")+1, d[2].count(":")) for d in datos]
    
    return(datos)

if __name__ == "__main__":
    pregunta_10()