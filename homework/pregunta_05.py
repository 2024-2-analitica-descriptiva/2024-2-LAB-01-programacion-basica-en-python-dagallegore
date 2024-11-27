"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    datos = open("files/input/data.csv","r").readlines()
    datos = [d.split("\t")[0:2] for d in datos]
    mayores = {}
    menores = {}
    for key, value in datos:
        if key in mayores:
            if mayores[key] < int(value):
                mayores[key] = int(value)
        else:
            mayores[key] = int(value)
        if key in menores:
            if menores[key] > int(value):
                menores[key] = int(value)
        else:
            menores[key] = int(value)
    lista = [(key, mayores.get(key), menores.get(key)) for key, _ in datos]
    return sorted(set(lista))


if __name__ == "__main__":
    pregunta_05()