from getopt import GetoptError
import socket,json,getopt
from model import MyEncoder
import csv, zipfile,sys
from random import randint
from multiprocessing import Process

def createSocketCliente():  # función que permite crear Socket del Servidor
    try:
        variable = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print('Fallo al crear el socket!')
        sys.exit()
    return variable

def establecerConexion_Cliente(client):
    (opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:')
    for (op, ar) in opt:
        if op == '-a':
            a = str(ar)
        elif op == '-p':
            p = int(ar)
            print('Opcion -p exitosa!')
    print('Socket Creado!')
    host = a
    port = p
    client.connect((host, port))
    print('Socket conectado al host', host, 'en el puerto', port)
    return client

def ingresar_DatosTicket(): #función cliente que pide datos para crear el ticket
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

def imprimirTickets(tickets): # función del cliente
    for ticket in tickets:
        ticket_json = json.loads(ticket)
        print("\n", "Ticket_Id:", ticket_json['ticket_Id'], "Title: ", ticket_json['title'], "Author: ",
              ticket_json['author'],
              "Descripción: ", ticket_json['description'], "Estado: ", ticket_json['status'], "Fecha: ",
              ticket_json['date'])

def imprimirTicket(ticket):
    print("\n", "Ticket_Id:", ticket['ticket_Id'], "Title: ", ticket['title'], "Author: ",
          ticket['author'],
          "Descripción: ", ticket['description'], "Estado: ", ticket['status'], "Fecha: ",
          ticket['date'])

def exportarTickets(lista):
    with open("tickets.csv", "w", newline='') as f:
        fieldnames = ['ticket_Id', 'title', 'author', 'description', 'status','date']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for ticket in lista:
            ticket_dict = json.loads(ticket)
            writer.writerow(ticket_dict)
    jungle_zip = zipfile.ZipFile('tickets.zip' + str(randint(1,10000)), 'w')
    jungle_zip.write('tickets.csv', compress_type=zipfile.ZIP_DEFLATED)
    jungle_zip.close()

def menu_editar(ticket): #función, menu para editTicket
    ticket_json = json.loads(ticket)
    print("\n","Ticket Para Editar")
    imprimirTicket(ticket_json)
    print("\n")
    salir = False
    while not salir:
        print("Opciones t (titulo) d(descripción) e(estado) s(salir)", "\n")
        opcion= input("Opción: ")
        print("")
        if opcion == 't':
            ticket_json['title'] = input("Titulo del Ticket: ")
        elif opcion == 'd':
            ticket_json['description'] = input("Descripción: ")
        elif opcion == 'e':
            ticket_json['status'] = input("Estado: ")
            if ticket_json['status'] == 'pendiente' or ticket_json['status'] == 'aprobado' or ticket_json['status'] == 'en-proceso':
                print("")
            else:
                print("Ha ingresado un estado que no corresponde")
                ticket_json['status'] = input("Estado: ")
        elif opcion =='s':
            salir=True
        else:
            print("Ingrese opciones válidas")
        print("\n","Ticket Editado")
        print("")
        imprimirTicket(ticket_json)
        print("")
        diccionario = {"ticket_Id":ticket_json['ticket_Id'],"title": ticket_json['title'], "author": ticket_json['author'], "description": ticket_json['description'], "status": ticket_json['status'], "date": ticket_json['date']}
        return diccionario

#Filtro

def filtarTickets(client): #función que permite filtrar Tickets por distintos argumentos
    print("Puede filtrar por autor, escriba -a + Nombre del Autor. Puede filtrar por Estado, escriba -e + Estado y puede filtrar por Fecha, "
          "escriba -f + fecha. Escriba -l para traer todos los Tickets. Puede filtrar de Manera Simultanea también mezclando los filtros, por ejemplo -e pendiente -a robot.")
    keywords = input("-a -e -f -l: ").split(" ") #se divide en 1 nomas la lista por ende puedo filtrar con mas de un argumento
    ticket = {}
    try:
        (opts, args) = getopt.getopt(keywords, 'p:a:a:e:f:l')
        for op, ar in opts:
            if op in ('-a'):
                argumento = ar
                ticket['author'] = argumento
            elif op in ['-e']:
                argumento = ar
                ticket['status'] = argumento
            elif op in ['-f']:  # consultar metodos de validaciones
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

def despacharTicketsCliente(client): #función que permite filtrar Tickets por distintos argumentos
    print("Puede exportar por autor, escriba -a + Nombre del Autor. Puede exportar por Estado, escriba -e + Estado y puede exportar por Fecha, "
          "escriba -f + fecha. Escriba -l para exportar todos los Tickets. Puede exportar Tickets de Manera Simultanea también.")
    keywords = input("-a -e -f -l: ").split(" ") #se divide en 1 nomas la lista por ende puedo filtrar con mas de un argumento
    ticket = {}
    try:
        (opts, args) = getopt.getopt(keywords, 'p:a:a:e:f:l')
        for op, ar in opts:
            if op in ('-a'):
                argumento = ar
                ticket['author'] = argumento
            elif op in ['-e']:
                argumento = ar
                ticket['status'] = argumento
            elif op in ['-f']:  # consultar metodos de validaciones
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
        despacharTicketsCliente(client)
    return ticket

def mandarArgumento(argumento, client):
    argumento_str = str(argumento)
    client.send(argumento_str.encode())

def recibirTickets(client, cantidad):
    cantidad_integer = int(cantidad) #cantidad que ingresa el user
    tickets = []
    for x in range(cantidad_integer):  # va cantidad integer
        tickets.append(client.recv(1024).decode())
    print("Tickets Agregados: ", len(tickets))
    imprimirTickets(tickets)

def recibirTicketsDespachados(client,cantidad):
    cantidad_integer = int(cantidad)  # cantidad que ingresa el user
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


def verificar_Cantidad_Cliente(cantidad): #tipo STR
    if cantidad == str(0):
        retorno = False
    else:
        retorno = True
    return retorno

