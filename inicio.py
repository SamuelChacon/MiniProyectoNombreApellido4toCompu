from persona import persona
MisContactos= ()

def crearContacto():
    print("Creando Contacto")
def main():
    op = 0
    while op != 7:
            print("-----------------Agenda 2022-----------------")
            print("1. Crear contacto")
            print("2. Buscar contacto")
            print("3. Ver contacto")
            print("4. Modificar contacto")
            print("5. Eliminar contacto")
            print("6. Crear reporte en HTMl")
            print("7. Salir del programa○\n\n: ")

            op = int(input("Ingrese el número de opción: "))
            if op == 1:
                numero = int(input("ingrese el numero de telefono: "))
                nombre = int(input("ingrese el nombre: "))
                direccion = int(input("ingrese la direccion: "))
                crearContacto(numero, nombre, direccion)
                crearContacto()

#iniciar programa
main()
