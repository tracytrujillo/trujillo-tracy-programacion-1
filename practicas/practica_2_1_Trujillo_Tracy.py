#Ejercicio: Datos personales
nombre = "Tracy"
edad = 22
ciudad = "Guadalajara"

print(nombre, edad, ciudad)

nombre = "Fer"
edad = 32
ciudad = "Tepic"

print(nombre, edad, ciudad)

#Ejercicio: Actualizar contador

contador = 0
contador = contador +1
print(contador)
contador = contador +1
print(contador)
contador = contador +1
print(contador)

#Ejercicio: Constante de conversion 
PULGADAS_A_CM = 2.54
pulgadas = 450
print(pulgadas * PULGADAS_A_CM)

PULGADAS_A_CM = 2.54
pulgadas = 56
print(pulgadas * PULGADAS_A_CM)

#Ejercicio: Area de un rectangulo 
base = 15
altura = 7
area = base * altura
perimetro = (base * 2) + (altura * 2)
print("el area es igual a", area)
print("el perimetro es igual a", perimetro)

base = 30
altura = 14
area = base * altura
perimetro = (base * 2) + (altura * 2)
print("el area es igual a", area)
print("el perimetro es igual a", perimetro)

#Ejercicio: Total con IVA
IVA = 0.16
precio = 135
total = precio + (precio * IVA)
print("precio + IVA:",precio, "total:", total)

precio = 45
total = precio + (precio * IVA)
print("precio + IVA:",precio, "total:", total)

#Ejercicio: Intercambio de valores
a = 25
b = 32

print("Antes a =", a, "b =", b)
temp = a
a = b
b = temp
print("despues del intercambio: a =", a, "b =" , b)

a = 89
b = 20

print("Antes a =", a, "b =", b)
temp = a
a = b
b = temp
print("despues del intercambio: a =", a, "b =" , b)


#Ejercicio: Identificar tipos con type()

entero = 22
decimal = 65.6
texto = "Creatividad"
booleano = False

print(type (entero))
print(type (decimal))
print(type (texto))
print(type (booleano))

entero = 67
decimal = 22.5
texto = "Comida"
booleano = True

print(type (entero))
print(type (decimal))
print(type (texto))
print(type (booleano))

#Ejercicio: Convertir tipos

nieves = "3"
texto_convertido = int(nieves)
print(texto_convertido, type(texto_convertido))

nieves = 3
numero_a_texto = str(nieves)
print(numero_a_texto, type(numero_a_texto))

cargadores = "2"
texto_convertido = int(cargadores)
print(texto_convertido, type(texto_convertido))

cargadores = 2
numero_a_texto = str(cargadores)
print(numero_a_texto, type(numero_a_texto))

#Ejercicio: Booleanos y comparaciones

vuelo = 12500
hospedaje = 18679
comparacion = vuelo < hospedaje
print(comparacion, type(comparacion))

protector_solar = 1299
crema = 890
comparacion = protector_solar < crema
print(comparacion, type(comparacion))







