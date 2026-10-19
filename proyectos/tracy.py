#Tracy Fernanda Trujillo Gonzalez
#Este programa sera capaz de capturar datos, validarlos, calcular el total e imprimirle un recibo.

#Captura de datos

cantidad = input("¿Cuantos productos vas a registrar?: ")
while not cantidad.isdigit():
  print("Error: debes ingresar un numero entero valido.")
  cantidad = input("¿Cuantos productos vas a registrar? ")

#Validacion 

cantidad = int(cantidad)
for i in range(cantidad):
  print(f"\n--- Producto {i + 1} ---")
  while True:
      nombre_producto = input("Ingresa el nombre del producto: ")
      if not any(c.isdigit() for c in nombre_producto) and nombre_producto.strip() != "":
          break
      print("Error: el nombre no debe contener numeros ni estar vacio.")
  

  #Calculos
  #Con decimales
while True:
  try:
    precio_producto = float(input("Ingresa el precio del producto:"))
    break 
  except ValueError: 
      print("Error: debes ingresar un numero valido para el precio.")

#Enteros
while True:
    cantidad_producto = input("Ingresa la cantidad de este producto: ")
    if cantidad_producto.isdigit():
        cantidad_producto: int(cantidad_producto)
        break
    print("Error: Debes ingresar un numero entero valido.")
