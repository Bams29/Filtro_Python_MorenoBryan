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
        "tiempo_afiliado":0,
        "categoria":"cliente nuevo",
        "historial_servicios":{},
        "reportes":{}
    }
    clientes = cargar_datos()
    clientes.append(nuevo_cliente)
    guardar_datos(clientes)

#----------------actualizar-----------    
def editar_cliente(dni_cliente, nueva_informacion):
    clientes = cargar_datos()
    for clientes in clientes:
        if clientes["dni"] == dni_cliente:
            clientes.update(nueva_informacion)
            guardar_datos(clientes)
            print(f"Información del cliente con dni {dni_cliente} actualizada correctamente.")
            return
        
#--------------Menu-------------------
        
print("1. añadir un nuevo cliente")
print("2. actualizar un cliente")
opcion = input("\nSeleccione una opción (1-14): ")

if opcion == "1":
    agregar_cliente()
elif opcion == "2":
            dni_cliente = input("Ingrese el dni del cliente que desea editar: ")
            nueva_informacion = {
                "nombres": input("Ingrese el nuevo nombre del cliente: "),
                "apellidos": input("Ingrese los nuevos apellidos del cliente: "),
                "direccion": input("Ingrese la nueva dirección del cliente: "),
                "telefono": input("Ingrese el nuevo teléfono celular del cliente: "),
                "estrato": input("Ingrese el nuevo estrato del cliente: "),
                "tiempo_afiliado": 0,
                "categoria": "cliente nuevo",
                "historial_servicios": {},
                "reportes": {}
            }






