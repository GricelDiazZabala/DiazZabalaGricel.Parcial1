# 1. Crear una función llamada aplicarAumento que reciba como parámetro el precio
# de un producto y devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main.

def aplicarAumento(precio):
    aumento = precio * 0.05
    precio_con_aumento = precio + aumento
    return precio_con_aumento

#ejemplo de uso

precio_base = input("Ingrese el precio base: ")
precio_con_aumento = aplicarAumento(precio_base)
print(precio_con_aumento)