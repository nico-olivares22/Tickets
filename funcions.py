from model import *
from db_config import *
from datetime import datetime,date
import socket

"""def crearTicket(lista): #funcion server
    ticket = Ticket(title=lista['title'], author=lista['author'], description=lista['description'],
                    status=lista['status'],date=date.today())
    session.add(ticket)
    session.commit()"""

"""def listarTickets_Server():
    tickets = session.query(Ticket).all()
    return tickets"""

"""def listarTickets(): # función del cliente
    page_tam = 0 #tickets por página
    page = 1 #pagina
    tickets = session.query(Ticket).all() #consulta
    size_lista = len(tickets) #tamaño de la lista
    while size_lista > page_tam:
        input("Enter: ")
        page_tam = page_tam + 5
        for ticket in tickets[:page_tam]:
            ticket_objeto = {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),
                             "title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author),
                             "description": print("Descripción: ", ticket.description),
                             "status": print("Estado: ", ticket.status),
                             "date": print("Fecha: ", str(ticket.date)), "": print("")}
        page = page + 1

    if size_lista < page_tam: #una pagina, hay que testearlo
        for ticket in tickets[0:page_tam]:
                ticket_objeto= {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),"title": print("Título: ",ticket.title), "author": print("Autor: ",ticket.author), "description": print("Descripción: ", ticket.description), "status": print("Estado: ",ticket.status),
                            "date": print("Fecha: ",str(ticket.date)), "":print("")}
    session.commit() #sino no se actualizaba el listar cuando estaba corriendo el cliente."""

"""def ingresar_DatosTicket(): #función cliente que pide datos para crear el ticket
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
    return ticket"""

"""def editTicket(id): #función del cliente para editar tickets
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
            if lista.status == 'pendiente' or lista.status == 'aprobado' or lista.status == 'en proceso':
                print("")
            else:
                print("Ha ingresado un estado que no corresponde")
                lista.status = input("Estado: ")
        elif opcion == 'f':
            lista.date = str(date.today())#probar despues
        elif opcion =='s':
            salir=True
        else:
            print("Ingrese opciones válidas")
        print("")
        print("Ticket Editado")
        print("")
        ticket = {"ticked_Id": print("Ticked_Id: ", lista.ticket_Id), "title": print("Título: ", lista.title),
                         "author": print("Autor: ", lista.author),
                         "description": print("Descripción: ", lista.description),
                         "status": print("Estado: ", lista.status),
                         "date": print("Fecha: ", str(lista.date)), "": print("")}"""





"""def broadcast(self, message):
            #Sending message to all clients
            for client in self.clients:
                client.send(message)

def imprimirTickets(tickets):
    tickets_por_pagina = 10 #tickets por página
    page = 0 #pagina
    size_lista = len(tickets) #tamaño de la lista
    while size_lista > tickets_por_pagina:
        input("Enter: ")

        for ticket in tickets[0:tickets_por_pagina]:
            print("")
            print("Ticket_Id: ", ticket['ticket_Id'], "Title: ", ticket['title'], "Author: ", ticket['author'],
                  "Descripción: ", ticket['description'], "Estado: ", ticket['status'], "Fecha: ", ticket['date'])
            print("")
        page = page + 1
        tickets_por_pagina = tickets_por_pagina + 1
        print("Pagina:", page)
        print("Tamaño: ", tickets_por_pagina)

    if size_lista < tickets_por_pagina: #una pagina, hay que testearlo
        for ticket in tickets[0:tickets_por_pagina]:
            print("")
            print("Ticket_Id:", ticket['ticket_Id'], "Title: ", ticket['title'], "Author: ", ticket['author'],
                  "Descripción: ", ticket['description'], "Estado: ", ticket['status'], "Fecha: ", ticket['date'])
            print("")
    return tickets"""


"""def imprimirTicketsFiltrados(tickets): 1
    for ticket in tickets:
        print("\n", "Ticked_Id: ", ticket['ticket_Id'], "Título: ", ticket['title'], "Autor: ", ticket['author'], "Descripción: ", ticket['description'],
              "Estado: ", ticket['status'], ticket['date'])"""

"""def recibirTickets_Filtro(client, cantidad): 2 sirven para lo mismo pero no se usan
    cantidad_integer = int(cantidad) #cantidad que ingresa el user
    tickets = []
    for x in range(cantidad_integer):  # va cantidad integer
        tickets.append(client.recv(1024).decode())
    print("Tickets Agregados: ", len(tickets))
    imprimirTickets(tickets)"""


"""def filtrarTickets_Server(sock):
    argumento = recibirArgumento(sock)
    print("Argumento Recibido: ", argumento)
    cadena = "-a -e -f -c ".split(" ")
    (opts, args) = getopt.getopt(cadena,'aefc')
    print("OPTS: ", opts)
    print("ARGS: ", args)
    tickets = []
    for op,ar in opts:
        if op in ['-a']:
            print("Entrando AUtor")
            tickets.append(filtrarByAuthor(argumento=argumento))
        elif op in ['-e']:
            print("Entrando Estado")
            tickets.append(filtrarByStatus(argumento=argumento))
        elif op in ['-f']:
            fecha = ar
            print("ENtrando FECHA")
            tickets.append(filtrarByFecha(argumento=fecha))
        elif op in ['-c']:
            break
        else:
            print("Opcion Incorecta")
    return tickets"""

"""if 'author' in ticket_loads and 'status' in ticket_loads:
    print("ENTRANDO AE")
    tickets = filtrarByAuthorAndEstado(argumento=ticket_loads['author'], argumento2=ticket_loads['status'])
elif 'author' and 'date' in ticket_loads:
    print("ENTRANDO AF")"""