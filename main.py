import json


def cargar_datos():
    try:
        with open("clientes.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_datos(datos):
    with open("clientes.json", "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=2, ensure_ascii=False)
#----------nuevo cliente------

def agregar_cliente():
    nuevo_cliente = {
        "dni": input("Ingrese el número de Identificación del cliente: "),
        "nombres": input("Ingrese el nombre del cliente: "),
        "apellidos": input("Ingrese los apellidos del cliente: "),
        "direccion": input("Ingrese la dirección del cliente: "),
        "telefono": input("Ingrese el teléfono celular del cliente: "),
        "estrato": input("Ingrese el estrato del cliente: "),
        "riesgo": input("Ingrese el riesgo del cliente: "),
        "tiempo_afiliado":0,
        "categoria":"cliente nuevo",
        "historial_servicios":{},
        "reportes":{}
    }
    clientes = cargar_datos()
    clientes.append(nuevo_cliente)
    guardar_datos(clientes)
    






#--------------Menu-------------------

