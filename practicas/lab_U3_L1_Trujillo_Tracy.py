#LAB U3 Comparaciones multiples


#Ejercicio: Clasificacion edad


edad = int(input("¿Que edad tienes? "))
if edad < 13:
    print("niño")
elif 13 <= edad <= 17:
     print("adolescente")
else:
     print("adulto")


#Ejercicio: Validar acceso (usuario y contraseña)


usuario_correcto ="hellokitty56"
contraseña_correcta ="sanriocnmnroll19"

usuario  = str(input("Ingrese su usuario: "))
contraseña = str(input("Ingresa tu contraseña: "))

if usuario == "" and contraseña == "":
    print("Error. Los campos no pueden estar en blanco.")
elif usuario == usuario_correcto and contraseña == contraseña_correcta:
     print("Acceso concedido. Bienvenido. ")
elif usuario == usuario_correcto and contraseña != contraseña_correcta:
     print("Contraseña incorrecta. ")
elif usuario != usuario_correcto and contraseña == contraseña_correcta:
    print("Usuario no encontrado. ")



#Ejercicio: Calculadora de envio 


paquete_kg = float(input("Ingrese el peso de su paquete en kg: "))

if paquete_kg <= 1:
    costo = 50
elif paquete_kg <= 5:
    costo = 90
else:
    costo = 150

if paquete_kg > 10:
    costo = costo * 0.90   
    print("¡Aplicó descuento del 10%!")

print("El costo de envío es: $", costo)


#Ejercicio: Clasificar la temperatura

temperatura_grados = float(input("Ingrese temperatura en grados: "))

if temperatura_grados <10:
  clasificacion = "frio"
elif 10 <= temperatura_grados < 25:
    clasificacion = "templado"
else:
    clasificacion = "calor"

print("La temperatura es:", clasificacion)


#Ejercicio: Calificacion con letras

calificacion = float(input("Ingresa tu calificacion del 0 a 100: "))


if calificacion >=90:
  print("Tu calificacion es: A")
elif calificacion >=80:
  print("Tu calificacion es: B")
elif calificacion >= 70:
    print("Tu calificación es: C")
elif calificacion >= 60:
    print("Tu calificación es: D")
else:
    print("Tu calificación es: F")


#Ejercicio: Descuento por monto de compra

monto_de_compra = float(input("Ingrese monto de compra: "))

if monto_de_compra > 500:
    porcentaje = 20
elif monto_de_compra > 200:
    porcentaje = 10
else:
    porcentaje = 0

descuento = monto_de_compra * porcentaje / 100
total = monto_de_compra - descuento

print("Tu descuento es de:", porcentaje, "%")
print("Total a pagar: $", total)



#Ejercicio: Validar un rango con comparacion encadenada

numero = float(input("Ingrese un número: "))

if 1 <= numero <= 100:
    print("El número", numero, "está en rango")
else:
    print("El número", numero, "NO está en rango")



#Ejercicio:Clasificar el IMC

peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))
imc = peso / estatura ** 2

if imc < 18.5:
    clasificacion = "bajo peso"
elif imc < 25:
    clasificacion = "normal"
elif imc < 30:
    clasificacion = "sobrepeso"
else:
    clasificacion = "obesidad"

print("Tu IMC es:", round(imc, 2))
print("Clasificación:", clasificacion)


#Ejercicio: Tarifas de electricidad

consumo = float(input("Ingrese su consumo mensual en kWh: "))

if consumo <= 150:
    costo = consumo * 1.20
elif consumo <= 300:
    costo = 150 * 1.20 + (consumo - 150) * 1.80
else:
    costo = 150 * 1.20 + 150 * 1.80 + (consumo - 300) * 2.50

print("Consumo:", consumo, "kWh")
print("Costo total: $" + str(costo))






