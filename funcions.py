from model import *
from db_config import *
from datetime import datetime
import getopt, sys, json

def crearTicket(lista):
    ticket = Ticket(title=lista['title'], author=lista['author'], description=lista['description'],
                    status=lista['status'], date=datetime.now())
    session.add(ticket)
    session.commit()


def listarTickets():  # función del cliente
    tickets = session.query(Ticket).all()
    for ticket in tickets:
         ticket_objeto= {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),"title": print("Título: ",ticket.title), "author": print("Autor: ",ticket.author), "description": print("Descripción: ", ticket.description), "status": print("Estado: ",ticket.status),
                        "date": print("Fecha: ",str(ticket.date)), "":print("")}
    session.commit() #sino no se actualizaba el listar cuando estaba corriendo el cliente.




def filtarTickets():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'a:e:f:p:')
    if opt == 'FILTRAR':
        for (op, ar) in opt:
            if ar =='-a':
                argumento = str(ar)
                filtrarByAuthor()
            elif op == '-e':
                argumento= ar
                argumento=filtrarByStatus()
            elif op == '-f':
                argumento = ar
                argumento=filtrarByFecha()
            else:
                print("OPCION NO VÁLIDA por parte del filtro")


def filtrarByAuthor():
    #tickets_author = session.query(Ticket).filter_by(author=Ticket.author) #problema con el filtro, trae todos los tickets por algun motivo
    tickets_auhor = session.query(Ticket).filter_by(edi)
    for ticket in tickets_author:
         ticket_objeto= {"title": print("Título: ",ticket.title), "author": print("Autor: ",ticket.author), "description": print("Descripción: ", ticket.description), "status": print("Estado: ",ticket.status),
                        "date": print("Fecha: ",str(ticket.date)), "":print("")}
def filtrarByStatus():
    status = session.query(Ticket).filter(Ticket.status)
    for ticket in status:
         ticket_objeto= {"title": print("Título: ",ticket.title), "author": print("Autor: ",ticket.author), "description": print("Descripción: ", ticket.description), "status": print("Estado: ",ticket.status),
                        "date": print("Fecha: ",str(ticket.date)), "":print("")}


def filtrarByFecha():
    session.query(Ticket).filter(Ticket.date)

"""def myconverter(o): #función serialización de fecha
    if isinstance(o, datetime.now()):
        return o.__str__()"""

"""'ticket_Id: ', ticket['ticket_Id'])
        print('title: ', ticket['title'])
        print('author: ', ticket['author'])
        print('description: ', ticket['description'])
        print('status: ', ticket['status'])
        print('date: ', ticket['date'])
        print(tickets)"""

def editTicket(id):
    print("")
    ticket = session.query(Ticket).get(id)
    ticket_objeto = {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id), "title": print("Título: ", ticket.title),
                     "author": print("Autor: ", ticket.author),
                     "description": print("Descripción: ", ticket.description),
                     "status": print("Estado: ", ticket.status),
                     "date": print("Fecha: ", str(ticket.date)), "": print("")}
    menu_editar(ticket)
    session.commit()


def menu_editar(lista):
    salir = False
    while not salir:
        print("Opciones t (titulo) a(autor) d(descripción) e(estado) f(fecha) s(salir)")
        opcion= input("Opción: ")
        if opcion == 't':
            lista.title= input("Titulo del Ticket: ")
        elif opcion == 'a':
            lista.author= input("Autor del Ticket: ")
        elif opcion == 'd':
            lista.description= input("Descripción: ")
        elif opcion == 'e':
            lista.status = input("Estado: ")
        elif opcion == 'f':
            lista.date = str(datetime.now())
        elif opcion =='s':
            salir=True
        else:
            print("Ingrese opciones válidas")
        ticket = {"title": lista.title, "author": lista.author, "description": lista.description, "status": lista.status, "date": lista.date}
        print("Ticket Editado")
        print(ticket)




""" LOGICA DEL GETOPT
keywords = input("-t -a -d -e -f: ") #lista con argumentos para el editado
    (opts, args) = getopt.getopt(keywords, 'p:a:t:a:d:e:f') #los opts son los argumentos que vienen del cliente
    for op in keywords.split():
        if op=='-t':
            ticket.title = op
        elif op == '-a':
            ticket.author = op
        elif op == "-e":
            ticket.status = op
        elif op == "-d":
             ticket.description = op
        elif op == "-f":
             op = str(datetime.now())
        else:
            print("Opción inválida")
            break
"""