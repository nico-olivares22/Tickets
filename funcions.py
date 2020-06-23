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
    print("Puede filtrar por autor, escriba -a + Nombre del Autor. Puede filtrar por Estado, escriba -e + Estado y puede filtrar por Fecha, escriba -f + fecha.")
    keywords = input("-a -e -f: ").split(" ",1) #se divide en 1 nomas la lista por ende puedo filtrar con mas de un argumento
    print("")
    (opts, args) = getopt.getopt(keywords, 'p:a:a:e:f')
    for op,ar in opts:
        if op in ('-a'):
            author =ar
            print("Argumento: " +ar)
            filtrarByAuthor(ticket=author)
        elif op in ['-e']:
            status = ar
            filtrarByStatus(ticket=status)
        elif op in ['-f']:
            date = ar
            filtrarByFecha(ticket=date)
        else:
            print("Opción Incorrecta")


def filtrarByAuthor(ticket):
    tickets_author = session.query(Ticket).filter_by(author=ticket)
    for ticket in tickets_author:
         ticket_objeto= {"title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author), "description": print("Descripción: ", ticket.description), "status": print("Estado: ", ticket.status),
                        "date": print("Fecha: ", str(ticket.date)), "":print("")}
    session.commit()
def filtrarByStatus(ticket):
    status = session.query(Ticket).filter_by(status=ticket)
    for ticket in status:
         ticket_objeto= {"title": print("Título: ",ticket.title), "author": print("Autor: ",ticket.author), "description": print("Descripción: ", ticket.description), "status": print("Estado: ",ticket.status),
                        "date": print("Fecha: ",str(ticket.date)), "":print("")}
    session.commit()
def filtrarByFecha(ticket):
    dates = session.query(Ticket).filter_by(date = ticket)
    for ticket in dates:
        ticket_objeto = {"title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author),
                         "description": print("Descripción: ", ticket.description),
                         "status": print("Estado: ", ticket.status),
                         "date": print("Fecha: ", str(ticket.date)), "": print("")}
    session.commit()

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
