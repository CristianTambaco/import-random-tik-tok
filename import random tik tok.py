import random
import os
from os import system

userRegistro=""
passwordRegistro=""

print("Bienvenido a tik tok")
print("Si tienes una cuenta ingrese si ")
print("Si no tiene una cuenta ingrese no ")
login=input("Ingrese la palabra: ")

if login=="no":
    print("Para crear una cuenta, ingresa los siguientes datos")
    correo=input("Ingresa tu correo electronico: ")
    userRegistro=input("Ingresa tu nombre de usuario: ")
    passwordRegistro=input("Ingresa tu contraseña: ")
    codigoAcceso = random.randint(1000,9999)
    print("Codigo de acceso es: " ,codigoAcceso)
    print("Felicidades, ya puedes iniciar sesion")
    
    if login=="no":
        print()
        codigo= int(input("Por favor, ingresa el codigo enviado al correo: "))
        while codigoAcceso != codigo:
            print("Error, verifique el codigo de acceso")
            codigo= int(input("Por favor, ingresa el codigo enviado al correo: "))
    print("Login")

print("Bienvenido")