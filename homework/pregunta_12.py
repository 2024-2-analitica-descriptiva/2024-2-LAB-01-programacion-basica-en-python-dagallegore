"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    datos = open("files/input/data.csv","r").readlines()
    datos = [d.split("\t") for d in datos]
    datos = [[d[0]] + [d[4][:-1]] for d in datos]
    print(datos)
    suma = {}
    for lista in datos:
        #print(lista)
        lista = [tuple(lista)]
        #print(lista)
        for key, value in lista:
            value = value.replace(",",":")
            value = value.split(":")
            print(key)
            c = 0
            for v in value:
                if c%2 == 1:
                    if key in suma:
                        suma[key] += int(v)
                    else:
                        suma[key] = int(v)
                c += 1
    return(dict(sorted(suma.items())))

if __name__ == "__main__":
    pregunta_12()