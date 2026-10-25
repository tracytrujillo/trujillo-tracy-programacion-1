#Tracy Fernanda Trujillo Gonzalez
#Programacion I
#Este programa sera capaz de capturar datos, validarlos.
#Calcula subtotal, IVA (16%) y total, e imprime un recibo de compra.

#Captura de datos
cantidad = input("¿Cuántos productos vas a registrar?: ")
while not cantidad.isdigit() or int(cantidad) == 0:
    print("Error: debes ingresar un número entero válido.")
    cantidad = input("¿Cuántos productos vas a registrar?: ")

cantidad = int(cantidad)
productos = []
subtotal_general = 0

for i in range(cantidad):
    print(f"\n--- Producto {i + 1} ---")

    #Validacion 
    #Nombre sin numeros ni vacios 
    while True:
        nombre_producto = input("Ingresa el nombre del producto: ")
        if not any(c.isdigit() for c in nombre_producto) and nombre_producto.strip() != "":
            break
        print("Error: el nombre no debe contener números ni estar vacío.")

    #Precio (con decimales)
    while True:
        try:
            precio_producto = float(input("Ingresa el precio del producto: "))
            break
        except ValueError:
            print("Error: debes ingresar un número válido para el precio.")

    #Cantidad (entero)
    while True:
        cantidad_producto = input("Ingresa la cantidad de este producto: ")
        if cantidad_producto.isdigit():
            cantidad_producto = int(cantidad_producto)
            break
        print("Error: debes ingresar un número entero válido.")
    #Calculos
    subtotal_producto = precio_producto * cantidad_producto
    subtotal_general += subtotal_producto
    productos.append((nombre_producto, precio_producto, cantidad_producto, subtotal_producto))

iva = subtotal_general * 0.16
total = subtotal_general + iva

#RECIBO
print("\n" + "=" * 45)
print("RECIBO")
print("=" * 45)
for nombre, precio, cant, sub in productos:
    print(f"{nombre:<15} {cant:>3} x ${precio:>8.2f} = ${sub:>9.2f}")
print("-" * 45)
print(f"{'Subtotal:':<30} ${subtotal_general:>10.2f}")
print(f"{'IVA (16%):':<30} ${iva:>10.2f}")
print(f"{'TOTAL A PAGAR:':<30} ${total:>10.2f}")
print("=" * 45)

print("Gracias por tu compra  (ᗒᗨᗕ)")


