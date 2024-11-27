"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    datos = open("files/input/data.csv","r").readlines()
    datos = [d.split("\t")[4] for d in datos]
    datos = [d[:-1] for d in datos]
    datos = [d.split(",") for d in datos]
    #print(datos)
    mayores = {}
    menores = {}
    claves = []
    for sublist in datos:
        sublist = [s.split(":") for s in sublist]
        
        sublist = [tuple(s) for s in sublist]
        #print(sublist)
        
        for key, value in sublist:
            if key not in claves:
                claves.append(key)
            if key in mayores and mayores[key] < int(value):
                mayores[key] = int(value)
            elif key not in mayores:
                mayores[key] = int(value)
            if key in menores and menores[key] > int(value):
                menores[key] = int(value)
            elif key not in menores:
                menores[key] = int(value)
    print(mayores)
    rta = [(key, menores.get(key), mayores.get(key)) for key in claves]
    return(sorted(rta))


if __name__ == "__main__":
    pregunta_06()