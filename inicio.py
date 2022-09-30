from persona import persona
MisContactos= []

def crearContacto(numero, nombre, direccion):
    MisContactos.append(persona(numero, nombre, direccion))
    print("Contacto almacenado....")

def buscarcontacto(nombre):
    if len(MisContactos) == 0:
        print("La lista esta vacía, no hay contactos que buscar...")
    else:
        encontrado = False
        for i in range(len(MisContactos)):
            if MisContactos[i].vernombre() == nombre:
                print("El telefono es " , MisContactos[i].vernumero())
                print("La direccion es " , MisContactos[i].verdireccion())
                encontrado = True
                break    
            else:
                encontrado = False
        if encontrado == False:
            print("Dato no existente...")        
    
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
            print("7. Salir del programa\n\n")
            op = int(input("Ingrese el número de opción: "))
            if op == 1:
                numero = int(input("ingrese el numero de telefono: "))
                nombre = input("ingrese el nombre: ")
                direccion = input("ingrese la direccion: ")
                crearContacto(numero, nombre, direccion)
            elif op ==2:
                nombre = input("ingrese el nombre del contacto a buscar: ")
                buscarcontacto(nombre) 
             
main()
