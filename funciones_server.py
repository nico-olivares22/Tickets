from model import *
from db_config import *
from datetime import date
import socket, json

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

def editarTicketServer(id, valores):
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

def filtrarByAuthor(argumento,ticket):  # permite filtrar tickets por autor
    ticket = ticket.filter(Ticket.author == argumento)
    recorrerVariable(ticket)
    return ticket

def filtrarByStatus(argumento,ticket):  # permite filtrar tickets por estado
    ticket = ticket.filter(Ticket.status == argumento)
    recorrerVariable(ticket)
    return ticket

def filtrarByFecha(argumento,ticket):  # permite filtrar tickets por fecha
    ticket = ticket.filter(Ticket.date == argumento)
    recorrerVariable(ticket)
    return ticket

def filtrarTickets_Server(sock):
    ticket = recibirArgumento(sock)
    ticket_loads = json.loads(ticket)
    tickets = session.query(Ticket).filter()
    for k,v in dict(ticket_loads).items():
        if k == 'author':
            tickets = filtrarByAuthor(ticket_loads['author'], tickets)
        if k == 'status':
            tickets = filtrarByStatus(ticket_loads['status'], tickets)
        if k == 'date':
            tickets = filtrarByFecha(ticket_loads['date'], tickets)
    return tickets

def recibirArgumento(sock):
    argumento = sock.recv(1024).decode()
    return argumento

