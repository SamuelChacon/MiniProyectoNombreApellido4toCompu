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
    
def mostrarcontactos():
    if len(MisContactos) == 0:
        print("La lista esta vacía, no hay contactos que buscar...")
    else:
        for i in range(len(MisContactos)):
            print("nombre: ", MisContactos[i].vernombre(), "direccion", MisContactos[i].verdireccion(), "telefono", MisContactos[i].vernumero())   

def modificarcontacto(nombre):
    if len(MisContactos) == 0:
        print("La lista esta vacía, no hay contactos que buscar...")
    else:
        encontrado = False
        posicion = None
        for i in range(len(MisContactos)):
            if MisContactos[i].vernombre() == nombre:
               posicion = i 
               encontrado = True
               break    
            else:
                encontrado = False
        if encontrado:
            nuevonumero = int(input("ingrese el nuevo numero: "))
            nuevonombre = input("ingrese nuevo nombre: ")
            nuevadireccion = input("ingrese la nueva direccion: ")
            MisContactos[posicion].modificarnumero(nuevonumero)
            MisContactos[posicion].modificarnombre(nuevonombre)
            MisContactos[posicion].modificardireccion(nuevadireccion)
            print("datos actualizados con exito...")
        else:
            print("dato no encontrado...")

def eliminarcontacto(nombre):
    if len(MisContactos) == 0:
        print("La lista esta vacía, no hay contactos que buscar...")
    else:
        encontrado = False
        posicion = None
        for i in range(len(MisContactos)):
            if MisContactos[i].vernombre() == nombre:
               posicion = i 
               encontrado = True
               break    
            else:
                encontrado = False
        if encontrado:
            MisContactos.pop(posicion)
            print("dato eliminado con exito...")
        else:
            print("dato no encontrado...")

def crearreporte():
    documento = open("reporte contactos.html", "w")
    documento.write("<!doctype html>\n")
    documento.write("<html\n")
    documento.write("</head>\n")
    documento.write("\t<title>Agenda 2022</title>\n")
    documento.write("</head>\n")
    documento.write("body>/n")
    documento.write("\t<center>\n")
    documento.write("\t<Mis contactos</h1\n")
    documento.write("\<table border=1>\n")
    documento.write("\t\t<tr>\n")
    documento.write("\t\t\t<td>Numero de telefono</td<td>Nombre</td><td>Direccion</td>\n")
    for i in range(len(MisContactos)):
        documento.write("\t\t<tr>\n")
        documento.write("\t\t\t<td>" +str(MisContactos[i].vernumero()) +"</td><td>" + MisContactos[i].vernombre() + "</td><td>" + MisContactos[i].verdireccion()+"</td>")
        documento.write("\t\t<tr>\n")


        documento.write("\t\t<tr>\n")
        documento.write("\t<table>\n")
        documento.write("\t<center>\n")
        documento.write("/body>\n") 
        documento.write("</html>")
        documento.close()
        print("reporte html creado con exito...")

    print("creando reporte html")             
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
            elif op == 3:
                mostrarcontactos()
            elif op ==4:
                nombre = input("ingrese el nombre del contacto: ")
                modificarcontacto(nombre)
            elif op == 5:
                nombre = input("ingrese el nombre del contacto: ")
                eliminarcontacto(nombre)  
            elif op == 6:
                crearreporte()
            elif op == 7:
                print("programa terminado...")
            else:
                print("opcion incorrecta...")                    

             
main()
