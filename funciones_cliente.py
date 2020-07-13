from getopt import GetoptError
import socket,json,getopt
from model import MyEncoder
import csv

def ingresar_DatosTicket(): #función cliente que pide datos para crear el ticket
    print("Ingrese datos del Ticket")
    title = input("Título del Ticket: ")
    author = input("Autor del Ticket: ")
    description = input("Descripción del Ticket: ")
    status = input("Estado del Ticket: ")
    if status == 'pendiente' or status == 'en proceso' or status == 'aprobado':
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
    """with open("tickets.csv", "w") as f:
        wr = csv.writer(f, delimiter="\n")
        wr.writerow(lista)"""
    with open("tickets.csv", "w", newline='') as f:
        fieldnames = ['ticket_Id', 'title', 'author', 'description', 'status','date']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for ticket in lista:
            ticket_dict = json.loads(ticket)
            writer.writerow(ticket_dict)

def menu_editar(ticket): #función, menu para editTicket
    ticket_json = json.loads(ticket)
    print("\n","Ticket Para Editar")
    imprimirTicket(ticket_json)
    print("\n")
    salir = False
    while not salir:
        print("Opciones t (titulo) a(autor) d(descripción) e(estado) s(salir)", "\n")
        opcion= input("Opción: ")
        print("")
        if opcion == 't':
            ticket_json['title'] = input("Titulo del Ticket: ")
        elif opcion == 'a':
            ticket_json['author'] = input("Autor del Ticket: ")
        elif opcion == 'd':
            ticket_json['description'] = input("Descripción: ")
        elif opcion == 'e':
            ticket_json['status'] = input("Estado: ")
            if ticket_json['status'] == 'pendiente' or ticket_json['status'] == 'aprobado' or ticket_json['status'] == 'en proceso':
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
          "escriba -f + fecha. Puede filtrar de Manera Simultanea también mezclando los filtros, por ejemplo -e pendiente -a robot.")
    keywords = input("-a -e -f -c: ").split(" ") #se divide en 1 nomas la lista por ende puedo filtrar con mas de un argumento
    ticket = {}
    try:
        (opts, args) = getopt.getopt(keywords, 'p:a:a:e:f:c')
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
            elif op in ['-c']:
                break
            else:
                print("Opción Incorrecta")
    except GetoptError:
        print("Error, Opción Mal Introducida")
    ticket_dict = json.dumps(ticket,cls=MyEncoder)
    mandarArgumento(ticket_dict,client)
    return ticket

def mandarArgumento(argumento, client):
    argumento_str = str(argumento)
    client.send(argumento_str.encode())