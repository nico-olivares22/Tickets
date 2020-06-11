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
        print("Id del Ticket: ", ticket.ticket_Id)
        print("Title: ", ticket.title)
        print("Author: ", ticket.author)
        print("Description: ", ticket.description)
        print("Status: ", ticket.status)
        print("Date: ", ticket.date)
    return {'tickets': [ticket.a_json() for ticket in tickets]}


def filtarTickets():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'a,e,f,p:')
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

