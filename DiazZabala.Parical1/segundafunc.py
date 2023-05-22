# 2. Crear una función que se llame reemplazarCaracteres que reciba una
# cadena de caracteres como primer parámetro, un carácter como segundo y otro carácter  como tercero,
# la misma deberá reemplazar cada ocurrencia del segundo parámetro por el tercero y devolver la cantidad
# de veces que se reemplazo ese carácter  en la cadena

def reemplazarCaracteres(cadena, caracter_original, caracter_nuevo):
    cantidad_reemplazos = cadena.count(caracter_original)
    cadena_modificada = cadena.replace(caracter_original, caracter_nuevo)
    return cantidad_reemplazos, cadena_modificada

#ejemplo de uso
cadena = "Hola mundo"
caracter_original = "o"
caracter_nuevo = "i"

cantidad_reemplazos, cadena_modificada = reemplazarCaracteres(cadena, caracter_original, caracter_nuevo)
print("Cantidad de reemplazos:", cantidad_reemplazos)
print("Cadena modificada:", cadena_modificada)
