import threading
from funciones_server import *
import json

serversocket = createSocketServer()
establecerConexion_Server(serversocket)

def th_server(sock,addr):
    """
    Función del Servidor encargada de interpretar los comandos enviados por el Cliente.
    Args:
        sock: socket aceptado del cliente
        addr: dirección IP y puerto del Cliente
    """
    print("Iniciando thread...\n")
    while True:
        opcion = sock.recv(1024)
        fecha = date.today() #fecha de operación
        print('Cliente %s:%s' % (addr[0], addr[1]))
        print("Opción: " + opcion.decode()) #opción que viene desde el cliente
        print("Fecha: ", fecha) #imprimir fecha
        print("")
        historial_server(fecha=fecha, opcion=opcion.decode(), address=addr)
        if opcion.decode() == ('-i') or opcion.decode() == ('--insertar'):
            ticket = sock.recv(1024).decode()
            ticket_dict = json.loads(ticket)
            crearTicket(ticket_dict)
            print("Ticket creado por el Cliente %s:%s" %(addr), "\n")

        elif opcion.decode() == ('-l') or opcion.decode() == ('--listar'):
            tickets = listarTicketsServer() #trae los tickets de la Base
            cantidad_tickets = str(len(tickets))
            sock.send(cantidad_tickets.encode())
            cantidad = sock.recv(1024).decode() #recibe la cantidad que ingreso el usuario
            traerTicketsPorCantidad(tickets, sock, cantidad)
            print("Cliente %s:%s ha listado los Tickets Disponibles" %(addr), "\n")

        elif opcion.decode() == ('-f') or opcion.decode() == ('--filtrar'):
            tickets_filtrados = filtrarTickets_Server(sock)
            tickets_filtrados = tickets_filtrados.all()
            proporcion = len(tickets_filtrados)
            sock.send(str(proporcion).encode())
            prueba = verificar_Cantidad_Servidor(proporcion) #linea agregada para verificar cantidad
            if prueba == False:
                continue
            cantidad_recibida = sock.recv(1024).decode()
            traerTicketsPorCantidad(tickets_filtrados,sock,cantidad_recibida)
            print("Cliente %s:%s ha filtrado Tickets " % (addr), "\n")

        elif opcion.decode() == ('-e') or opcion.decode() == ('--editar'):
            ticket_ID = sock.recv(1024).decode()
            print("Id Recibido: ", ticket_ID)
            verificar = verificar_ticketID(ticket_ID)
            if verificar == False:
                continue
            ticket = traerTicketPorID(ticket_ID)
            ticket_objeto = json.dumps(ticket, cls=MyEncoder)
            sock.send(ticket_objeto.encode())  # manda el ticket en json al cliente
            ticket_editado = sock.recv(1024).decode()  # recibe el ticket editado
            editarTicketServer(ticket_ID, ticket_editado)
            print("Cliente %s:%s ha Editado un Ticket" % (addr), "\n")

        elif (opcion.decode() == ('-d') or opcion.decode() == ('--despachar')):
            tickets_filtrados = filtrarTickets_Server(sock)
            tickets_filtrados = tickets_filtrados.all()
            proporcion = len(tickets_filtrados)
            sock.send(str(proporcion).encode())
            prueba = verificar_Cantidad_Servidor(proporcion)  # linea agregada para verificar cantidad
            if prueba == False:
                continue
            cantidad_recibida = sock.recv(1024).decode()
            traerTicketsPorCantidad(tickets_filtrados, sock, cantidad_recibida)
            print("Cliente %s:%s ha Exportado Tickets" % (addr), "\n")

        elif opcion.decode() == ('-c') or opcion.decode() == ('--cerrar'):
            print("Cliente %s:%s DESCONECTADO \n" %(addr))
            break
        else:
            print('\nOpción Inválida!\n')

ThreadCount = 0
try:
    while True:
            clientsocket, addr = serversocket.accept() #accept espera una conexión entrante. Esta función devuelve una conexión abierta entre el servidor y cliente, junto con la dirección del cliente.
            print("\nObteniendo conexión desde %s:%d\n" % (addr[0],addr[1]))
            ThreadCount += 1
            print('Thread Number: ' + str(ThreadCount), "\n")
            th = threading.Thread(target=th_server, args=(clientsocket, addr,)).start()
except KeyboardInterrupt:
    clientsocket.close()