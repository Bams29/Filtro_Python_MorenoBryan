import json


with open("clientes.json", "r") as file:
    clientes = json.load(file)

#----------nuevo cliente------
    
nuevo_cliente = {}

clientes['nombre'] = input("ingrese el nombre del nuevo cliente: ")
clientes['apellido'] = input("ingrese el apellido del nuevo cliente: ")
clientes['edad'] = input("ingrese la edad del nuevo usuario: ")
clientes['dni'] = input("ingresa el nuemero de identificacion del usuario: ")
clientes['telefono'] = input("ingrese el telefono del nuevo cliente: ")
clientes['direccion'] = input("ingrese la direccion del nuevo cliente: ")
clientes['estrato'] = input("ingresa el estrato del nuevo cliente: ")
clientes['categoria'] = "cliente nuevo"
clientes['años afiliado'] = 0




