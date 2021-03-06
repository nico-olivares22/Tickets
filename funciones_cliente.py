from getopt import GetoptError
import socket,json,getopt
from model import MyEncoder
import csv, zipfile,sys
from random import randint
from multiprocessing import Process

def createSocketCliente():
    """
    Función encargada de crear el Socket desde el lado del Cliente.
    Returns: variable
    """
    try:
        variable = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print('Fallo al crear el socket!')
        sys.exit()
    return variable

def establecerConexion_Cliente(client):
    """
    Función que se encarga de establecer la conexión de el Cliente con el Servidor.
    Args:
        client: socket cliente
    Returns: client
    """
    (opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:')
    for (op, ar) in opt:
        if op == '-a':
            a = str(ar)
        elif op == '-p':
            p = int(ar)
            print('Opción -p exitosa!')
    print('Socket Creado!')
    host = a
    port = p
    client.connect((host, port)) #se conecta a la dirección del servidor y al puerto del servidor
    print('Socket conectado al host', host, 'en el puerto', port)
    return client

def ingresar_DatosTicket():
    """
    Función que permite al cliente ingresar los datos del Ticket a crear.
    Returns: ticket (diccionario)
    """
    print("Ingrese datos del Ticket")
    title = input("Título del Ticket: ")
    author = input("Autor del Ticket: ")
    description = input("Descripción del Ticket: ")
    status = input("Estado del Ticket: ")
    if status == 'pendiente' or status == 'en-proceso' or status == 'aprobado':
        print("")
    else:
        print("Ha ingresado un estado que no corresponde")
        status = input("Estado del Ticket: ")
    ticket = {"title": title, "author": author, "description": description, "status": status}
    return ticket

def imprimirTickets(tickets):
    """
    Función que permite imprimir una lista de Tickets.
    Args:
        tickets: lista con los tickets
    """
    for ticket in tickets:
        ticket_dict = json.loads(ticket)
        print("\n", "Ticket_Id:", ticket_dict['ticket_Id'], "Title: ", ticket_dict['title'], "Author: ",
              ticket_dict['author'],
              "Descripción: ", ticket_dict['description'], "Estado: ", ticket_dict['status'], "Fecha: ",
              ticket_dict['date'])

def imprimirTicket(ticket):
    """
    Función que se encarga de imprimir un ticket en Particular.
    Args:
        ticket: (diccionario)
    """
    print("\n", "Ticket_Id:", ticket['ticket_Id'], "Title: ", ticket['title'], "Author: ",
          ticket['author'],
          "Descripción: ", ticket['description'], "Estado: ", ticket['status'], "Fecha: ",
          ticket['date'])

def exportarTickets(lista):
    """
    Permite exportar Tickets en un archivo csv comprimido en zip.
    Args:
        lista: lista con tickets
    """
    with open("tickets.csv", "w", newline='') as f:
        fieldnames = ['ticket_Id', 'title', 'author', 'description', 'status','date']
        writer = csv.DictWriter(f, fieldnames=fieldnames) #escribe datos a un archivo CSV, f es el archivo, fieldnames define la secuencia en que sos escritos los datos.
        writer.writeheader() #escribe una fila con los nombres.
        for ticket in lista:
            ticket_dict = json.loads(ticket)
            writer.writerow(ticket_dict) #va escribiendo por fila cada ticket
    jungle_zip = zipfile.ZipFile('tickets.zip' + str(randint(1,10000)), 'w')
    jungle_zip.write('tickets.csv', compress_type=zipfile.ZIP_DEFLATED)
    jungle_zip.close()

def menu_editar(ticket):
    """
    Permite que el usuario ingrese los datos que quiera cambiar en el Ticket.
    Args:
        ticket: ticket en str
    Returns: diccionario
    """
    ticket_dict = json.loads(ticket)
    print("\n","Ticket Para Editar")
    imprimirTicket(ticket_dict)
    print("\n")
    salir = False
    while not salir:
        print("Opciones t (titulo) d(descripción) e(estado) s(salir)", "\n")
        opcion= input("Opción: ")
        print("")
        if opcion == 't':
            ticket_dict['title'] = input("Titulo del Ticket: ")
        elif opcion == 'd':
            ticket_dict['description'] = input("Descripción: ")
        elif opcion == 'e':
            ticket_dict['status'] = input("Estado: ")
            if ticket_dict['status'] == 'pendiente' or ticket_dict['status'] == 'aprobado' or ticket_dict['status'] == 'en-proceso':
                print("")
            else:
                print("Ha ingresado un estado que no corresponde")
                ticket_dict['status'] = input("Estado: ")
        elif opcion =='s':
            salir=True
        else:
            print("Ingrese opciones válidas")
        print("\n","Ticket Editado")
        print("")
        imprimirTicket(ticket_dict)
        print("")
        diccionario = {"ticket_Id":ticket_dict['ticket_Id'],"title": ticket_dict['title'], "author": ticket_dict['author'], "description": ticket_dict['description'], "status": ticket_dict['status'], "date": ticket_dict['date']}
        return diccionario

#Filtro

def filtarTickets(client):
    """
    Permite al usuario ingresar argumentos para Filtrar Tickets.
    Args:
        client: socket cliente
    Returns:ticket (diccionario)
    """
    print("Puede filtrar por autor, escriba -a + Nombre del Autor. Puede filtrar por Estado, escriba -e + Estado y puede filtrar por Fecha, "
          "escriba -f + fecha en formato año-mes-día. Escriba -l para traer todos los Tickets. Puede filtrar de Manera Simultánea también mezclando los filtros, por ejemplo -e pendiente -a robot.")
    keywords = input("-a -e -f -l: ").split(" ") #se pasa el string a lista y se divide la lista en espacios
    ticket = {}
    try:
        (opts, args) = getopt.getopt(keywords, 'a:e:f:l')
        for op, ar in opts:
            if op in ('-a'):
                argumento = ar
                ticket['author'] = argumento
            elif op in ['-e']:
                argumento = ar
                ticket['status'] = argumento
            elif op in ['-f']:
                argumento = ar
                ticket['date'] = argumento
            elif op in ['-l']:
                break
            else:
                print("Opción Incorrecta")
        ticket_dict = json.dumps(ticket, cls=MyEncoder)
        mandarArgumento(ticket_dict, client)
    except GetoptError:
        print("Error, Opción Mal Introducida")
        filtarTickets(client) #recursividad
    return ticket

def despacharTicketsCliente(client):
    """
    Permite al usuario ingresar argumentos para Exportar Tickets.
    Args:
        client: socket cliente
    Returns:ticket (diccionario)
    """
    print("Puede exportar por autor, escriba -a + Nombre del Autor. Puede exportar por Estado, escriba -e + Estado y puede exportar por Fecha, "
          "escriba -f + fecha en formato año-mes-día. Escriba -l para exportar todos los Tickets. Puede exportar Tickets de Manera Simultánea también.")
    keywords = input("-a -e -f -l: ").split(" ") #se pasa el string a lista y se divide la lista en espacios
    ticket = {}
    try:
        (opts, args) = getopt.getopt(keywords, 'a:e:f:l')
        for op, ar in opts:
            if op in ('-a'):
                argumento = ar
                ticket['author'] = argumento
            elif op in ['-e']:
                argumento = ar
                ticket['status'] = argumento
            elif op in ['-f']:
                argumento = ar
                ticket['date'] = argumento
            elif op in ['-l']:
                break
            else:
                print("Opción Incorrecta")
        ticket_json = json.dumps(ticket, cls=MyEncoder)
        mandarArgumento(ticket_json, client)
    except GetoptError:
        print("Error, Opción Mal Introducida")
        despacharTicketsCliente(client)
    return ticket

def mandarArgumento(argumento, client):
    """
    Se encarga de mandar argumento al Servidor.
    Args:
        argumento: lo que el cliente quiera mandar
        client: socket cliente
    """
    argumento_str = str(argumento)
    client.send(argumento_str.encode())

def recibirTickets(client, cantidad):
    """
    Se encarga de recibir la cantidad ingresada por el usuario para luego imprimir esa cantidad de Tickets.
    Args:
        client: socket cliente
        cantidad: cantidad ingresada por el usuario
    """
    cantidad_integer = int(cantidad) #cantidad que ingresa el user
    tickets = []
    for x in range(cantidad_integer):  # va cantidad integer
        tickets.append(client.recv(1024).decode())
    print("Tickets Agregados: ", len(tickets))
    imprimirTickets(tickets)

def recibirTicketsDespachados(client,cantidad):
    """
    Se encarga de recibir la cantidad ingresada por el usuario para luego imprimir esa cantidad de Tickets.
    Args:
        client: socket cliente
        cantidad: cantidad ingresada por el usuario
    """
    cantidad_integer = int(cantidad)
    tickets = []
    if cantidad_integer == 0:
        print("NO hay tickets con ese/esos argumentos para Exportar")
    else:
        for x in range(cantidad_integer):  # va cantidad integer
            tickets.append(client.recv(1024).decode())
        print("Tickets Agregados: ", len(tickets))
        imprimirTickets(tickets)
        proceso = Process(target=exportarTickets, args=(tickets,))
        proceso.start()


def verificar_Cantidad_Cliente(cantidad):
    """
    Función encargada de verificar la cantidad mandanda por el Servidor.
    Args:
        cantidad: cantidad de tickets disponibles
    Returns: retorno False cuando no hay tickets, si hay tickets devuelve True
    """
    if cantidad == str(0):
        retorno = False
    else:
        retorno = True
    return retorno

