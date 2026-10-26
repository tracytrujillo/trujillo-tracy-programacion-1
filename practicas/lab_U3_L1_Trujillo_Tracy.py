#LAB U3 Comparaciones multiples


#Ejercicio: Clasificacion edad

#Enunciado: Pide la edad de una persona y clasifica como ´niño´ (menor de 13 años), adolescente (13 a 17) o adulto (18 o mas)

edad = int(input("¿Que edad tienes? "))
if edad < 13:
    print("niño")
elif 13 <= edad <= 17:
     print("adolescente")
else:
     print("adulto")


#Ejercicio: Validar acceso (usuario y contraseña)

#Enunciado: Define en tu codigo un usuario y una contraseña correctos (por ejemplo, en dos variables). Pide al usuario que los escriba y comparalos.
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
#Enunciado: Pide el peso de un paquete en kilogramos y calcula el costo de envio segun estas reglas: 




