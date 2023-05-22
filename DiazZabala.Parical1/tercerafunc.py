# 3. Crear una función que se llame ordenarCaracteres que reciba una cadena de caracteres como parámetro
# y su responsabilidad es ordenar los caracteres de manera ascendente dentro de la cadena. 
# Ejemplo si le pasamos "algoritmo" la deja como "agilmoort"

def ordenarCaracteres(cadena):
    caracteres_ordenados = sorted(cadena)
    cadena_ordenada = "".join(caracteres_ordenados)
    return cadena_ordenada

#ejemplo de uso

cadena_original = "algoritmo"
cadena_ordenada = ordenarCaracteres(cadena_original)
print(cadena_ordenada)

cadena_original = "computadora"
cadena_ordenada = ordenarCaracteres(cadena_original)
print(cadena_ordenada)


