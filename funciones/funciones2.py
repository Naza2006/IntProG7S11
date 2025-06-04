def calcular_monto(precio = 0, cantidad = 0):
    return precio * cantidad

precio = float(input("Ingrese el precio del producto: "))
cantidad = float(input("Ingrese la cantidad del producto: "))

resultado = calcular_monto(precio, cantidad)
print(f"El monto total a pagar es de : {resultado}")

precio = 50
cantidad = 10

