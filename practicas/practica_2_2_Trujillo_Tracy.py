#Ejercicio: "¿Es par o impar?"
numero = 14
print(numero % 2 == 0)

numero = 13
print(numero % 2 == 0)

#Ejercicio> Concatenar vs, sumar

lapices = "2"
borradores = "6"

print(lapices + borradores)
print(int(lapices) + int(borradores))

ventiladores = "56"
celulares = "35"

print(ventiladores + celulares)
print(int(ventiladores) + int(celulares))

#Comentario: en uno simplemente se unen sin sumarse porque se considera cadena de texto debido a las comillas, al hacer la transicion con int, ahora se pueden sumar y hacer operaciones con ellos.

#Ejercicio: Mini reporte de un perfil 

nombre = "Tracy"
edad = 22
estatura = 1.70
es_estudiante = True

#Ejercicio: Mini reporte de un perfil
nombre = "Tracy"
edad = 22
estatura = 1.70
es_estudiante = True

print("Nombre:", nombre, type(nombre))
print("Edad:", edad, type(edad))
print("Estatura:", estatura, type(estatura))
print("¿Es estudiante?:", es_estudiante, type(es_estudiante))


# Ejercicio — Mini reporte de un perfil
nombre = "Sophia"
edad = 44
estatura = 1.89
es_estudiante = False

print("Nombre:", nombre, type(nombre))
print("Edad:", edad, type(edad))
print("Estatura:", estatura, type(estatura))
print("¿Es estudiante?:", es_estudiante, type(es_estudiante))




#Ejercicio: Operadores artimeticos basicos 

a = 34
b = 78

print("Suma:" , a + b)
print("Resta:" , a - b)
print("Multiplicacion: " , a * b)
print("Division:" , a / b)

a = 6789
b = 4755

print("Suma:" , a + b)
print("Resta:" , a - b)
print("Multiplicacion: " , a * b)
print("Division:" , a / b)

a = 657
b = 389

print("Suma:" , a + b)
print("Resta:" , a - b)
print("Multiplicacion: " , a * b)
print("Division:" , a / b)


#Ejercicio: Division entera y modulo

a = 34
b = 78

print(a / b)
print(a // b)
print(a % b)

##/ realiza la division exacta y // (division entera) elimina los decimales

a = 78
b = 34
print(a / b)
print(a // b)
print(a % b)

#Ejercicio: Operadores relacionales

item1 = 45
item2 = 67

mayor = item1 > item2
menor = item1 < item2
igual = item1 == item2
diferente = item1 != item2

print("Probando con números distintos (45 y 67) ")
print("¿Es mayor?", mayor)
print("¿Es menor?", menor)
print("¿Son iguales?", igual)
print("¿Son diferentes?", diferente)


item1 = 99
item2 = 89

mayor = item1 > item2
menor = item1 < item2
igual = item1 == item2
diferente = item1 != item2

print("Probando con números distintos (99 y 89) ")
print("¿Es mayor?", mayor)
print("¿Es menor?", menor)
print("¿Son iguales?", igual)
print("¿Son diferentes?", diferente)




#Ejercicio: Operadores logicos 
a = 19
b = 87

resultado_and = (a < 6) and (b > 34)
resultado_or = (a > 67) or (b > 13)
resultado_not = not (a == b)

print("Resultado con and:", resultado_and)
print("Resultado con or:", resultado_or)
print("Resultado con not:", resultado_not)


a = 987
b = 56

resultado_and = (a < 9) and (b > 46)
resultado_or = (a > 78) or (b > 147)
resultado_not = not (a == b)

print("Resultado con and:", resultado_and)
print("Resultado con or:", resultado_or)
print("Resultado con not:", resultado_not)


#Ejercicio: Promedio y aprobacion

matematicas = 78
quimica = 98
biologia = 89

promedio = (matematicas + quimica + biologia) // 3
aprobado = promedio >= 80

print("Tu promedio es:", promedio)
print("Condicion:" , aprobado)

matematicas = 89
quimica = 45
biologia = 100

promedio = (matematicas + quimica + biologia) // 3
aprobado = promedio >= 80

print("Tu promedio es:" , promedio)
print("Condicion:" , aprobado)


#Ejercicio: Validacion y elegibilidad 

edad = 45
nacionalidad = "mexicana"
es_elegible = (edad > 17) and (nacionalidad == "mexicana")
print(es_elegible)


edad = 17
nacionalidad = "coreana"
es_elegible = (edad > 17) and (nacionalidad == "mexicana")
print(es_elegible)

#False
edad = 30
nacionalidad = "española"
es_elegible = (edad > 17) and (nacionalidad == "mexicana")
print(es_elegible)



















