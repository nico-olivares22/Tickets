from model import *
from db_config import *
from datetime import datetime,date
import socket

def crearTicket(lista): #funcion server
    ticket = Ticket(title=lista['title'], author=lista['author'], description=lista['description'],
                    status=lista['status'],date=date.today())
    session.add(ticket)
    session.commit()


def listarTickets():  # función del cliente
    tickets = session.query(Ticket).all()
    for ticket in tickets:
         ticket_objeto= {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),"title": print("Título: ",ticket.title), "author": print("Autor: ",ticket.author), "description": print("Descripción: ", ticket.description), "status": print("Estado: ",ticket.status),
                        "date": print("Fecha: ",str(ticket.date)), "":print("")}
    session.commit() #sino no se actualizaba el listar cuando estaba corriendo el cliente.

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

def editTicket(id): #función del cliente para editar tickets
    print("")
    ticket = session.query(Ticket).get(id)
    if session.query(Ticket).filter(Ticket.ticket_Id.ilike(id)).count()==0:
        print("No existe el ID Amigo")
    else:
        ticket_objeto = {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id), "title": print("Título: ", ticket.title),
                         "author": print("Autor: ", ticket.author),
                         "description": print("Descripción: ", ticket.description),
                         "status": print("Estado: ", ticket.status),
                         "date": print("Fecha: ", str(ticket.date)), "": print("")}
        menu_editar(ticket)
        session.commit()


def menu_editar(lista): #función, menu para editTicket
    salir = False
    while not salir:
        print("Opciones t (titulo) a(autor) d(descripción) e(estado) f(fecha) s(salir)")
        opcion= input("Opción: ")
        print("")
        if opcion == 't':
            lista.title= input("Titulo del Ticket: ")
        elif opcion == 'a':
            lista.author= input("Autor del Ticket: ")
        elif opcion == 'd':
            lista.description= input("Descripción: ")
        elif opcion == 'e':
            lista.status = input("Estado: ")

        elif opcion == 'f':
            lista.date = str(date.today())#probar despues
        elif opcion =='s':
            salir=True
        else:
            print("Ingrese opciones válidas")

        print("Ticket Editado")
        print("")
        ticket = {"ticked_Id": print("Ticked_Id: ", lista.ticket_Id), "title": print("Título: ", lista.title),
                         "author": print("Autor: ", lista.author),
                         "description": print("Descripción: ", lista.description),
                         "status": print("Estado: ", lista.status),
                         "date": print("Fecha: ", str(lista.date)), "": print("")}

def createSocketServer():
    variable = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return variable



    """def broadcast(self, message):
            #Sending message to all clients
            for client in self.clients:
                client.send(message)"""