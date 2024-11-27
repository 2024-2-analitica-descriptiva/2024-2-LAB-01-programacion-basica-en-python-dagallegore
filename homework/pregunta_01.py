"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    datos = open("files/input/data.csv","r").readlines()
    datos = [d.split("\t") for d in datos]
    valores = [int(d[1]) for d in datos]
    return sum(valores)

if __name__ == "__main__":
    pregunta_01()