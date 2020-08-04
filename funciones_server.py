from sqlalchemy.orm.exc import NoResultFound
from model import *
from db_config import *
from datetime import date
import socket, json,getopt,sys

def createSocketServer():
    """
    Función que permite crear Socket del Servidor.
    Returns:
        variable: socket creado del server
    """
    variable = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #se crear el socket servidor
    return variable

def establecerConexion_Server(serversocket):
    """
    Función encargada de establecer la conexión del Servidor con el socket creado anteriormente.
    Args:
        serversocket: socket del servidor creado
    """
    (opcion, arg) = getopt.getopt(sys.argv[1:], 'p:')
    for (op, ar) in opcion:
        if op == '-p':
            p = int(ar)
            print('Opción -p exitosa!')
        host = ""
        port = p
        serversocket.bind((host, port))  #se utiliza para asociar el conector con la dirección del servidor.
        serversocket.listen(1) #escucha a un cliente en simultáneo a la vez

def crearTicket(diccionario):
    """
    Permite insertar un Ticket a la Base de Datos.
    Args:
        diccionario: que es un diciconario con todos los datos cargados
    """
    ticket = Ticket(title=diccionario['title'], author=diccionario['author'], description=diccionario['description'],
                    status=diccionario['status'], date=date.today())
    session.add(ticket)
    session.commit()

def listarTicketsServer():
    """
    Función que permite listar todos los tickets de la Base de Datos.
    Returns: tickets (lista con todos los tickets)
    """
    tickets = session.query(Ticket).all()
    session.commit()
    return tickets

def editarTicketServer(id, valores):
    """
    Función que se encarga de guardar en la Base de Datos un Ticket Editado.
    Args:
        id: id del Ticket Editado
        valores: son los datos modificados por el usuario
    Returns:
    """
    ticket = session.query(Ticket).get(int(id))
    valores_json = json.loads(valores)
    ticket.title = valores_json['title']
    ticket.description = valores_json['description']
    ticket.status = valores_json['status']
    session.add(ticket)
    session.commit()
    return ticket

def traerTicketPorID(id):
    """
    Función que se encarga de traer un Ticket por ID.
    Args:
        id: id del Ticket
    Returns: ticket en JSON
    """
    ticket = session.query(Ticket).get(int(id))
    return ticket.toJSON()

def verificar_ticketID(ticket_ID):
    """
    Se encarga de Verificar si existe el ID ingresado en La Base de Datos.
    Args:
        ticket_ID: ID del Ticket ingresado
    Returns: retorno, True si existe, en caso contrario False
    """
    try:
        session.query(Ticket).filter(Ticket.ticket_Id == ticket_ID).one()
        retorno = True
    except NoResultFound:
        retorno = False
    return retorno

def filtrarByAuthor(argumento,ticket):
    """
    Permite Filtrar tickets por Autor.
    Args:
        argumento: argumento que ingreso el usuario
        ticket: query
    Returns: ticket
    """
    ticket = ticket.filter(Ticket.author == argumento)
    return ticket

def filtrarByStatus(argumento,ticket):
    """
    Permite Filtrar Tickets por Estado.
    Args:
        argumento: argumento que ingreso el usuario
        ticket: query
    Returns: ticket
    """
    ticket = ticket.filter(Ticket.status == argumento)
    return ticket

def filtrarByFecha(argumento,ticket):
    """
    Permite Filtrar Tickets por Fecha.
    Args:
        argumento: argumento que ingreso el usuario
        ticket: query
    Returns: ticket
    """
    ticket = ticket.filter(Ticket.date == argumento)
    return ticket

def filtrarTickets_Server(sock):
    """
    Función encargada de Aplicar los distintos Filtros.
    Args:
        sock: socket del servidor creado
    Returns: lista de tickets con filtros listos
    """
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
    """
    Función que se encarga de recibir un argumento mandado por el Cliente.
    Args:
        sock: socket del servidor creado
    Returns:
    """
    argumento = sock.recv(1024).decode()
    return argumento

def historial_server(fecha,opcion,address):
    """
    Función encargada de administrar un historial de las distintas operaciones que hace el Cliente.
    Args:
        fecha: fecha de la operación
        opcion: operación del cliente
        address: ip con puerto del cliente
    Returns:
    """
    archivo = open('historial_server.log','a')
    archivo.write(f"\nFecha: {fecha}, Opción: {opcion}, Cliente %s:%d" %(address))
    archivo.close()

def traerTicketsPorCantidad(lista, sock, cantidad):
    """
    Función encargada de traer Tickets por la cantidad ingresada por el usuario y mandar esa cantidad de Tickets.
    Args:
        lista: lista con tickets
        sock: socket del servidor creado
        cantidad: cantidad ingresada por el usuario
    """
    cantidad_integer = int(cantidad)
    for ticket in lista[0:cantidad_integer]:
        ticket_objeto = json.dumps(ticket,cls=MyEncoder)
        sock.send(ticket_objeto.encode()) #manda los tickets de la base de datos

def verificar_Cantidad_Servidor(cantidad):
    """
    Función que comprueba la cantidad de Tickets Disponibles.
    Args:
        cantidad: cantidad tickets disponibles
    Returns: retorno, False cuando no hay tickets, True cuando si hay
    """
    if cantidad == 0:
        retorno = False
    else:
        retorno = True
    return retorno

