import json


with open("clientes.json", "r") as file:
    clientes = json.load(file)
    
nuevo_cliente = {}

name = input("ingrese el nombre del nuevo cliente: ")
apellido = input("ingrese el apellido del nuevo cliente: ")
edad = input("ingrese la edad del nuevo usuario: ")
dni = input("ingresa el nuemero de identificacion del usuario: ")
telefono = input("ingrese el telefono del nuevo cliente: ")
direccion = input("ingrese la direccion del nuevo cliente: ")
estrato = input("ingresa el estrato del nuevo cliente: ")



with open("clientes.json", "w") as file:
    json.dump(nuevo_cliente, file, indent=4)


#----------nuevo cliente------


    






#--------------Menu-------------------

