from model import *
from db_config import *
from datetime import date
import socket, json, getopt


def createSocketServer():  # función que permite crear Socket del Servidor
    variable = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return variable

def crearTicket(lista):  # funcion server, que permite insertar un Ticket
    ticket = Ticket(title=lista['title'], author=lista['author'], description=lista['description'],
                    status=lista['status'], date=date.today())
    session.add(ticket)
    session.commit()

def listarTicketsServer():
    tickets = session.query(Ticket).all()
    session.commit()
    return tickets

# EDITAR TICKET CASI FUNCIONA
def editarTicketServer(id, valores):  ##llega bien el ticket pero no lo puedo guardar
    ticket = session.query(Ticket).get(int(id))
    valores_json = json.loads(valores)
    ticket.title = valores_json['title']
    ticket.author = valores_json['author']
    ticket.description = valores_json['description']
    ticket.status = valores_json['status']
    session.add(ticket)
    session.commit()
    return ticket

def traerTicketPorID(id):
    ticket = session.query(Ticket).get(int(id))
    if session.query(Ticket).filter(Ticket.ticket_Id.ilike(id)).count() == 0:
        print("No existe el ID Amigo")
    return ticket.toJSON()

# FILTRO
def recorrerVariable(variable):
    for ticket in variable:
        ticket_objeto = {"ticked_Id": ticket.ticket_Id,
                         "title": ticket.title, "author": ticket.author,
                         "description": ticket.description,
                         "status": ticket.status,
                         "date": str(ticket.date)}
        session.commit()
        return variable

def filtrarByAuthor(argumento):  # permite filtrar tickets por autor
    tickets_author = session.query(Ticket).filter(Ticket.author == argumento).all()
    recorrerVariable(tickets_author)
    return tickets_author

def filtrarByAuthorAndEstado(argumento, argumento2):
    tickets = session.query(Ticket).filter(Ticket.author == argumento, Ticket.status == argumento2)
    recorrerVariable(tickets)
    return tickets

def filtrarByStatus(argumento):  # permite filtrar tickets por estado
    status = session.query(Ticket).filter(Ticket.status == argumento).all()
    recorrerVariable(status)
    return status

def filtrarByFecha(argumento):  # permite filtrar tickets por fecha
    dates = session.query(Ticket).filter(Ticket.date == argumento).all()
    recorrerVariable(dates)
    return dates

def filtrarTickets_Server(sock):
    ticket = recibirArgumento(sock)
    ticket_loads = json.loads(ticket)
    print("LLEGANDO: ", ticket_loads)
    if 'author' in ticket_loads:
        print("1")
        tickets = filtrarByAuthor(argumento=ticket_loads['author'])
    if 'status' in ticket_loads:
        print("2")
        tickets = filtrarByStatus(argumento=ticket_loads['status'])
    if 'date' in ticket_loads:
        print("3")
        tickets = filtrarByFecha(argumento=ticket_loads['date'])

    return tickets

def recibirArgumento(sock):
    argumento = sock.recv(1024).decode()
    return argumento

