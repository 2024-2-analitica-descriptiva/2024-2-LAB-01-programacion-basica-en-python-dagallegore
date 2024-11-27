"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    datos = open("files/input/data.csv","r").readlines()
    datos = [d.split("\t")[4] for d in datos]
    datos = [d[:-1] for d in datos]
    datos = [d.split(",") for d in datos]
    rta = {}
    for sublist in datos:
        sublist = [s.split(":")[0] for s in sublist]
        for s in sublist:
            if s in rta:
                rta[s] += 1
            else:
                rta[s] = 1
    rta = sorted(rta.items())
    final = {}
    for r, value in rta:
        final[r] = value
    return(final)

if __name__ == "__main__":
    pregunta_09()