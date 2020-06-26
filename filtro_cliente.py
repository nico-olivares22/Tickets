import getopt
from db_config import *
from model import *

def recorrerVariable(variable):
    for ticket in variable:
        ticket_objeto = {"ticked_Id": print("Ticked_Id: ", ticket.ticket_Id),
                         "title": print("Título: ", ticket.title), "author": print("Autor: ", ticket.author),
                         "description": print("Descripción: ", ticket.description),
                         "status": print("Estado: ", ticket.status),
                         "date": print("Fecha: ", str(ticket.date)), "": print("")}
        session.commit()

def filtarTickets(): #función que permite filtrar Tickets por distintos argumentos
    print("Puede filtrar por autor, escriba -a + Nombre del Autor. Puede filtrar por Estado, escriba -e + Estado y puede filtrar por Fecha, escriba -f + fecha. Por último para cerra el filtro escriba -c")
    keywords = input("-a -e -f -c: ").split(" ",1) #se divide en 1 nomas la lista por ende puedo filtrar con mas de un argumento
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

def filtrarByAuthor(ticket): #permite filtrar tickets por autor
    tickets_author = session.query(Ticket).filter(Ticket.author==ticket)
    recorrerVariable(tickets_author)
def filtrarByStatus(ticket): #permite filtrar tickets por estado
    status = session.query(Ticket).filter(Ticket.status==ticket)
    recorrerVariable(status)
def filtrarByFecha(ticket): #permite filtrar tickets por fecha
    dates = session.query(Ticket).filter(Ticket.date==ticket)
    recorrerVariable(dates)

def menuFiltrarAuthor(argumento): #a los tickets filtrados por autor, se los puede filtrar por estado o fecha
    tickets_authors = session.query(Ticket).filter(Ticket.author == argumento) #traigo todos los tickets del autor ingresado
    print("¿Desea aplicar filtros a los tickets que filtró por autor?. Puede hacer -e + estado que quiera filtrar y -f + fecha que quiera filtrar. Presione -c para cerrar.")
    opciones = input("-e -f -c: ").split(" ",1)
    print("")
    (opts, args) = getopt.getopt(opciones, 'p:a:e:f:c')
    for op,ar in opts:
        if op in ['-e']:
            estado = ar
            tickets_estado = tickets_authors.filter(Ticket.status==estado)
            recorrerVariable(tickets_estado)
            filtrarAutorPorEstadoYFecha(variable=tickets_estado)
        elif op in ['-f']:
            fecha = ar
            tickets_fechas = tickets_authors.filter(Ticket.date==fecha)
            recorrerVariable(tickets_fechas)
            filtrarAutorporFechaYEstado(variable=tickets_fechas)
        elif op in ['-c']:
            break
        else:
            print("Opción Incorrecta")
    session.commit()

def filtrarAutorPorEstadoYFecha(variable): #a los tickets filtrados por autor y estado se los puede filtrar por fecha
    print("¿Desea aplicarle filtro por fecha a los Tickets que filtro por autor y estado?.Presione -f + fecha para hacerlo, sino -s para cerrar el Filtro.")
    eleccion = input("-f -s: ").split(" ",1)
    print(" ")
    (options, args) = getopt.getopt(eleccion, 'p:a:f:s')
    for op,ar in options:
        if op in ['-f']:
            fecha_ticket = ar
            tickets_fecha = variable.filter(Ticket.date==fecha_ticket)
            recorrerVariable(tickets_fecha)
        elif op in ['-s']:
            break
        else:
            print("Opción Incorrecta")
def filtrarAutorporFechaYEstado(variable): #a los tickets filtrados por autor y fecha se los puede filtrar por estado
    print("¿Desea aplicarle filtro por estado a los Tickets que filtro por autor y fecha?.Presione -e + estado para hacerlo, sino -s para cerrar el Filtro.")
    eleccion = input("-e -s: ").split(" ", 1)
    print(" ")
    (options, args) = getopt.getopt(eleccion, 'p:a:e:s')
    for op, ar in options:
        if op in ['-e']:
            estado_ticket = ar
            tickets_estado = variable.filter(Ticket.status == estado_ticket)
            recorrerVariable(tickets_estado)
        elif op in ['-s']:
            break
        else:
            print("Opción Incorrecta")

def menuFiltrarStatus(argumento): #a los tickets filtrados por estado, se los puede filtrar por autor o fecha
    tickets_status = session.query(Ticket).filter(Ticket.status == argumento) #traigo todos los tickets del autor ingresado
    print("¿Desea aplicar filtros a los tickets que filtró por estado?. Puede hacer -a + autor que quiera filtrar y -f + fecha que quiera filtrar. Presione -c para cerrar.")
    opciones = input("-a -f -c: ").split(" ",1)
    print("")
    (opts, args) = getopt.getopt(opciones, 'p:a:a:f:c')
    for op,ar in opts:
        if op in ['-a']:
            autor = ar
            tickets_autor = tickets_status.filter(Ticket.author==autor)
            recorrerVariable(tickets_autor)
            filtrarEstadoPorAutorYFecha(variable=tickets_autor)

        elif op in ['-f']:
            fecha = ar
            fechas = tickets_status.filter(Ticket.date==fecha)
            recorrerVariable(fechas)
            filtrarEstadoPorFechaYAutor(variable=fechas)
        elif op in ['-c']:
            break
        else:
            print("Opción Incorrecta")
    session.commit()

def filtrarEstadoPorAutorYFecha(variable): #a los tickets filtrados por estado y autor, se los puede filtrar por fecha
    print("¿Desea aplicarle filtro por fecha a los Tickets que filtro por estado y autor?.Presione -f + fecha para hacerlo, sino -s para cerrar el Filtro.")
    eleccion = input("-f -s: ").split(" ", 1)
    print(" ")
    (options, args) = getopt.getopt(eleccion, 'p:a:f:s')
    for op, ar in options:
        if op in ['-f']:
            fecha_ticket = ar
            tickets_fecha = variable.filter(Ticket.date == fecha_ticket)
            recorrerVariable(tickets_fecha)
        elif op in ['-s']:
            break
        else:
            print("Opción Incorrecta")

def filtrarEstadoPorFechaYAutor(variable): #a los tickets filtrados por estado y fecha se los puede filtrar por autor
    print("¿Desea aplicarle filtro por autor a los Tickets que filtro por estado y fecha?.Presione -a + autor para hacerlo, sino -s para cerrar el Filtro.")
    eleccion = input("-a -s: ").split(" ", 1)
    print(" ")
    (options, args) = getopt.getopt(eleccion, 'p:a:a:s')
    for op, ar in options:
        if op in ['-a']:
            author_ticket = ar
            tickets_author = variable.filter(Ticket.author == author_ticket)
            recorrerVariable(tickets_author)
        elif op in ['-s']:
            break
        else:
            print("Opción Incorrecta")


def menuFiltrarFecha(argumento): #a los tickets filtrados por fecha, se los puede filtrar por autor o estado
    tickets_date = session.query(Ticket).filter(Ticket.date == argumento) #traigo todos los tickets del autor ingresado
    print("¿Desea aplicar filtros a los tickets que filtró por Fecha?. Puede hacer -a + autor que quiera filtrar y -e + estado que quiera filtrar. Presione -c para cerrar.")
    opciones = input("-a -e -c: ").split(" ",1)
    (opts, args) = getopt.getopt(opciones, 'p:a:a:e:c')
    for op,ar in opts:
        if op in ['-a']:
            autor = ar
            tickets_autor = tickets_date.filter(Ticket.author==autor)
            recorrerVariable(tickets_autor)
            filtrarFechaPorAutorYEstado(variable=tickets_autor)
        elif op in ['-e']:
            estado = ar
            fechas = tickets_date.filter(Ticket.status==estado)
            recorrerVariable(fechas)
            filtrarFechaPorEstadoYAutor(variable=fechas)
        elif op in ['-c']:
            break
        else:
            print("Opción Incorrecta")
    session.commit()

def filtrarFechaPorAutorYEstado(variable): #a los tickets filtrados por fecha y autor, se los puede filtrar por estado
    print("¿Desea aplicarle filtro por estado a los Tickets que filtro por fecha y autor?.Presione -e + estado para hacerlo, sino -s para cerrar el Filtro.")
    eleccion = input("-e -s: ").split(" ", 1)
    print(" ")
    (options, args) = getopt.getopt(eleccion, 'p:a:e:s')
    for op, ar in options:
        if op in ['-e']:
            estado_ticket = ar
            tickets_estado = variable.filter(Ticket.status == estado_ticket)
            recorrerVariable(tickets_estado)
        elif op in ['-s']:
            break
        else:
            print("Opción Incorrecta")

def filtrarFechaPorEstadoYAutor(variable): #a los tickets filtrados por fecha y estado se los puede filtrar por autor
    print("¿Desea aplicarle filtro por autor a los Tickets que filtro por fecha y estado?.Presione -a + autor para hacerlo, sino -s para cerrar el Filtro.")
    eleccion = input("-a -s: ").split(" ", 1)
    print(" ")
    (options, args) = getopt.getopt(eleccion, 'p:a:a:s')
    for op, ar in options:
        if op in ['-a']:
            author_ticket = ar
            tickets_author = variable.filter(Ticket.author == author_ticket)
            recorrerVariable(tickets_author)
        elif op in ['-s']:
            break
        else:
            print("Opción Incorrecta")