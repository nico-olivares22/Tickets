from model import *
from db_config import *
from datetime import datetime,date
import getopt, sys, json

def crearTicket(lista):
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




"""def filtarTickets():
    print("Puede filtrar por autor, escriba -a + Nombre del Autor. Puede filtrar por Estado, escriba -e + Estado y puede filtrar por Fecha, escriba -f + fecha. Por último para cerra el filtro escriba -c")
    keywords = input("-a -e -f: ").split(" ",1) #se divide en 1 nomas la lista por ende puedo filtrar con mas de un argumento
    print("")
    (opts, args) = getopt.getopt(keywords, 'p:a:a:e:f:c')
    for op,ar in opts:
        if op in ('-a'):
            author =ar
            filtrarByAuthor(ticket=author)
            menuFiltrarAuthor(argumento=ar)
        elif op in ['-e']:
            status = ar
            filtrarByStatus(ticket=status)
            menuFiltrarStatus(argumento=ar)
        elif op in ['-f']: #consultar metodos de validaciones
            fecha = ar
            print("Fecha: " + fecha)
            filtrarByFecha(ticket=fecha)
            menuFiltrarFecha(argumento=ar)
        elif op in ['-c']:
            break
        else:
            print("Opción Incorrecta")

def filtrarByAuthor(ticket):
    tickets_author = session.query(Ticket).filter(Ticket.author==ticket)
    for ticket in tickets_author:
         ticket_objeto= {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),"title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author), "description": print("Descripción: ", ticket.description), "status": print("Estado: ", ticket.status),
                        "date": print("Fecha: ", str(ticket.date)), "":print("")}
    session.commit()
    return tickets_author
def filtrarByStatus(ticket):
    status = session.query(Ticket).filter(Ticket.status==ticket)
    for ticket in status:
         ticket_objeto= {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),"title": print("Título: ",ticket.title), "author": print("Autor: ",ticket.author), "description": print("Descripción: ", ticket.description), "status": print("Estado: ",ticket.status),
                        "date": print("Fecha: ",str(ticket.date)), "":print("")}
    session.commit()
def filtrarByFecha(ticket):
    dates = session.query(Ticket).filter(Ticket.date==ticket)
    for ticket in dates:
        ticket_objeto = {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),"title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author),
                         "description": print("Descripción: ", ticket.description),
                         "status": print("Estado: ", ticket.status),
                         "date": print("Fecha: ", str(ticket.date)), "": print("")}
    session.commit()

def menuFiltrarAuthor(argumento):
    tickets_authors = session.query(Ticket).filter(Ticket.author == argumento) #traigo todos los tickets del autor ingresado
    print("¿Desea aplicar filtros a los tickets que filtró por autor?. Puede hacer -e + estado que quiera filtrar y -f + fecha que quiera filtrar. Presione -c para cerrar.")
    opciones = input("-e -f -c: ").split(" ",1)
    print("")
    (opts, args) = getopt.getopt(opciones, 'p:a:e:f:c')
    for op,ar in opts:
        if op in ['-e']:
            estado = ar
            tickets_estado = tickets_authors.filter(Ticket.status==estado)
            for ticket in tickets_estado:
                ticket_objeto = {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),
                                 "title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author),
                                 "description": print("Descripción: ", ticket.description),
                                 "status": print("Estado: ", ticket.status),
                                 "date": print("Fecha: ", str(ticket.date)), "": print("")}
            session.commit()
            filtrarAutorPorEstadoYFecha(variable=tickets_estado)
        elif op in ['-f']:
            fecha = ar
            tickets_fechas = tickets_authors.filter(Ticket.date==fecha)
            for ticket in tickets_fechas:
                ticket_objeto = {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),
                                 "title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author),
                                 "description": print("Descripción: ", ticket.description),
                                 "status": print("Estado: ", ticket.status),
                                 "date": print("Fecha: ", str(ticket.date)), "": print("")}
            session.commit()
            filtrarAutorporFechaYEstado(variable=tickets_fechas)
        elif op in ['-c']:
            break
        else:
            print("Opción Incorrecta")
    session.commit()

def filtrarAutorPorEstadoYFecha(variable):
    print("¿Desea aplicarle filtro por fecha a los Tickets que filtro por autor y estado?.Presione -f + fecha para hacerlo, sino -s para cerrar el Filtro.")
    eleccion = input("-f -s: ").split(" ",1)
    print(" ")
    (options, args) = getopt.getopt(eleccion, 'p:a:f:s')
    for op,ar in options:
        if op in ['-f']:
            fecha_ticket = ar
            tickets_fecha = variable.filter(Ticket.date==fecha_ticket)
            for ticket in tickets_fecha:
                ticket_objeto = {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),
                                 "title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author),
                                 "description": print("Descripción: ", ticket.description),
                                 "status": print("Estado: ", ticket.status),
                                 "date": print("Fecha: ", str(ticket.date)), "": print("")}
            session.commit()
        elif op in ['-s']:
            break
        else:
            print("Opción Incorrecta")
def filtrarAutorporFechaYEstado(variable):
    print("¿Desea aplicarle filtro por estado a los Tickets que filtro por autor y fecha?.Presione -e + estado para hacerlo, sino -s para cerrar el Filtro.")
    eleccion = input("-e -s: ").split(" ", 1)
    print(" ")
    (options, args) = getopt.getopt(eleccion, 'p:a:e:s')
    for op, ar in options:
        if op in ['-e']:
            estado_ticket = ar
            tickets_estado = variable.filter(Ticket.status == estado_ticket)
            for ticket in tickets_estado:
                ticket_objeto = {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),
                                 "title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author),
                                 "description": print("Descripción: ", ticket.description),
                                 "status": print("Estado: ", ticket.status),
                                 "date": print("Fecha: ", str(ticket.date)), "": print("")}
            session.commit()
        elif op in ['-s']:
            break
        else:
            print("Opción Incorrecta")

def menuFiltrarStatus(argumento):
    tickets_status = session.query(Ticket).filter(Ticket.status == argumento) #traigo todos los tickets del autor ingresado
    print("¿Desea aplicar filtros a los tickets que filtró por estado?. Puede hacer -a + autor que quiera filtrar y -f + fecha que quiera filtrar. Presione -c para cerrar.")
    opciones = input("-a -f -c: ").split(" ",1)
    print("")
    (opts, args) = getopt.getopt(opciones, 'p:a:a:f:c')
    for op,ar in opts:
        if op in ['-a']:
            autor = ar
            tickets_autor = tickets_status.filter(Ticket.author==autor)
            for ticket in tickets_autor:
                ticket_objeto = {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),
                                 "title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author),
                                 "description": print("Descripción: ", ticket.description),
                                 "status": print("Estado: ", ticket.status),
                                 "date": print("Fecha: ", str(ticket.date)), "": print("")}
            session.commit()
            filtrarEstadoPorAutorYFecha(variable=tickets_autor)

        elif op in ['-f']:
            fecha = ar
            fechas = tickets_status.filter(Ticket.date==fecha)
            for ticket in fechas:
                ticket_objeto = {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),
                                 "title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author),
                                 "description": print("Descripción: ", ticket.description),
                                 "status": print("Estado: ", ticket.status),
                                 "date": print("Fecha: ", str(ticket.date)), "": print("")}
            session.commit()
            filtrarEstadoPorFechaYAutor(variable=fechas)
        elif op in ['-c']:
            break
        else:
            print("Opción Incorrecta")
    session.commit()

def filtrarEstadoPorAutorYFecha(variable):
    print("¿Desea aplicarle filtro por fecha a los Tickets que filtro por estado y autor?.Presione -f + fecha para hacerlo, sino -s para cerrar el Filtro.")
    eleccion = input("-f -s: ").split(" ", 1)
    print(" ")
    (options, args) = getopt.getopt(eleccion, 'p:a:f:s')
    for op, ar in options:
        if op in ['-f']:
            fecha_ticket = ar
            tickets_fecha = variable.filter(Ticket.date == fecha_ticket)
            for ticket in tickets_fecha:
                ticket_objeto = {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),
                                 "title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author),
                                 "description": print("Descripción: ", ticket.description),
                                 "status": print("Estado: ", ticket.status),
                                 "date": print("Fecha: ", str(ticket.date)), "": print("")}
            session.commit()
        elif op in ['-s']:
            break
        else:
            print("Opción Incorrecta")

def filtrarEstadoPorFechaYAutor(variable):
    print("¿Desea aplicarle filtro por autor a los Tickets que filtro por estado y fecha?.Presione -a + autor para hacerlo, sino -s para cerrar el Filtro.")
    eleccion = input("-a -s: ").split(" ", 1)
    print(" ")
    (options, args) = getopt.getopt(eleccion, 'p:a:a:s')
    for op, ar in options:
        if op in ['-a']:
            author_ticket = ar
            tickets_author = variable.filter(Ticket.author == author_ticket)
            for ticket in tickets_author:
                ticket_objeto = {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),
                                 "title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author),
                                 "description": print("Descripción: ", ticket.description),
                                 "status": print("Estado: ", ticket.status),
                                 "date": print("Fecha: ", str(ticket.date)), "": print("")}
            session.commit()
        elif op in ['-s']:
            break
        else:
            print("Opción Incorrecta")


def menuFiltrarFecha(argumento):
    tickets_date = session.query(Ticket).filter(Ticket.date == argumento) #traigo todos los tickets del autor ingresado
    print("¿Desea aplicar filtros a los tickets que filtró por Fecha?. Puede hacer -a + autor que quiera filtrar y -e + estado que quiera filtrar. Presione -c para cerrar.")
    opciones = input("-a -e -c: ").split(" ",1)
    (opts, args) = getopt.getopt(opciones, 'p:a:a:e:c')
    for op,ar in opts:
        if op in ['-a']:
            autor = ar
            tickets_autor = tickets_date.filter(Ticket.author==autor)
            for ticket in tickets_autor:
                ticket_objeto = {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),
                                 "title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author),
                                 "description": print("Descripción: ", ticket.description),
                                 "status": print("Estado: ", ticket.status),
                                 "date": print("Fecha: ", str(ticket.date)), "": print("")}
            session.commit()
            filtrarFechaPorAutorYEstado(variable=tickets_autor)
        elif op in ['-e']:
            estado = ar
            fechas = tickets_date.filter(Ticket.status==estado)
            for ticket in fechas:
                ticket_objeto = {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),
                                 "title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author),
                                 "description": print("Descripción: ", ticket.description),
                                 "status": print("Estado: ", ticket.status),
                                 "date": print("Fecha: ", str(ticket.date)), "": print("")}
            session.commit()
            filtrarFechaPorEstadoYAutor(variable=fechas)
        elif op in ['-c']:
            break
        else:
            print("Opción Incorrecta")
    session.commit()

def filtrarFechaPorAutorYEstado(variable):
    print("¿Desea aplicarle filtro por estado a los Tickets que filtro por fecha y autor?.Presione -e + estado para hacerlo, sino -s para cerrar el Filtro.")
    eleccion = input("-e -s: ").split(" ", 1)
    print(" ")
    (options, args) = getopt.getopt(eleccion, 'p:a:e:s')
    for op, ar in options:
        if op in ['-e']:
            estado_ticket = ar
            tickets_estado = variable.filter(Ticket.status == estado_ticket)
            for ticket in tickets_estado:
                ticket_objeto = {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),
                                 "title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author),
                                 "description": print("Descripción: ", ticket.description),
                                 "status": print("Estado: ", ticket.status),
                                 "date": print("Fecha: ", str(ticket.date)), "": print("")}
            session.commit()
        elif op in ['-s']:
            break
        else:
            print("Opción Incorrecta")

def filtrarFechaPorEstadoYAutor(variable):
    print("¿Desea aplicarle filtro por autor a los Tickets que filtro por fecha y estado?.Presione -a + autor para hacerlo, sino -s para cerrar el Filtro.")
    eleccion = input("-a -s: ").split(" ", 1)
    print(" ")
    (options, args) = getopt.getopt(eleccion, 'p:a:a:s')
    for op, ar in options:
        if op in ['-a']:
            author_ticket = ar
            tickets_author = variable.filter(Ticket.author == author_ticket)
            for ticket in tickets_author:
                ticket_objeto = {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),
                                 "title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author),
                                 "description": print("Descripción: ", ticket.description),
                                 "status": print("Estado: ", ticket.status),
                                 "date": print("Fecha: ", str(ticket.date)), "": print("")}
            session.commit()
        elif op in ['-s']:
            break
        else:
            print("Opción Incorrecta")"""


def editTicket(id):
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


def menu_editar(lista):
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

