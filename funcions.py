from model import *
from db_config import *
from datetime import datetime
import getopt, sys


def crearTicket(lista):
    ticket = Ticket(title=lista['title'], author=lista['author'], description=lista['description'],
                    status=lista['status'], date=datetime.now())
    session.add(ticket)
    session.commit()


def listarTickets():  # función del cliente
    tickets = session.query(Ticket).all()
    for ticket in tickets:
         ticket_objeto= {"title": print("Título: ",ticket.title), "author": print("Autor: ",ticket.author), "description": print("Descripción: ", ticket.description), "status": print("Estado: ",ticket.status),
                        "date": print("Fecha: ",str(ticket.date)), "":print("")}




def filtarTickets():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'a:e:f:p:')
    for (op, ar) in opt:
        if ar == '-a':
            filtrarByAuthor()
        elif ar == '-e':
            filtrarByStatus()
        elif ar == '-f':
            filtrarByFecha()


def filtrarByAuthor():
    session.query(Ticket).filter(Ticket.author)


def filtrarByStatus():
    session.query(Ticket).filter(Ticket.status)


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

