from model import *
import threading,time
from threading import Semaphore
from funciones_server import *
import json,getopt,sys

(opcion, arg) = getopt.getopt(sys.argv[1:], 'p:')

for (op, ar) in opcion:
    if op == '-p':
        p = int(ar)
        print('Opcion -p exitosa!')

def th_server(sock,addr, semaphore):
    print("Iniciando thread...\n")
    while True:
        opcion = sock.recv(1024)
        fecha = date.today() #fecha de operación
        print('Cliente %s:%s' % (addr[0], addr[1]))
        print("Opcion: " + opcion.decode()) #opción que viene desde el cliente
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
            proporcion = len(tickets_filtrados) #linea 1
            sock.send(str(proporcion).encode()) #linea 2
            cantidad_recibida = sock.recv(1024).decode() #linea 3
            traerTicketsPorCantidad(tickets_filtrados,sock,cantidad_recibida)
            print("Cliente %s:%s ha filtrado los Tickets Disponibles" % (addr), "\n")

        elif opcion.decode() == ('-e') or opcion.decode() == ('--editar'):
            ticket_ID = sock.recv(1024).decode()
            print("Id Recibido amigo: ", ticket_ID)
            semaphore.acquire()
            ticket = traerTicketPorID(ticket_ID)
            ticket_objeto = json.dumps(ticket,cls=MyEncoder)
            sock.send(ticket_objeto.encode()) #manda el ticket en json al cliente
            ticket_editado = sock.recv(1024).decode() #recibe el ticket editado
            editarTicketServer(ticket_ID,ticket_editado)
            semaphore.release()
            time.sleep(0.5)
            print("Cliente %s:%s ha editado un Ticket" % (addr), "\n")
        elif opcion.decode() == ('-c') or opcion.decode() == ('--cerrar'):
            print("Cliente %s:%s DESCONECTADO \n" %(addr))
            break
        else:
            print('\nOpcion invalida!\n')

serversocket = createSocketServer()

host = ""
port = p
ThreadCount = 0
serversocket.bind((host, port))  # linea de comandos, host y puerto
serversocket.listen(5)

def historial_server(fecha,opcion,address):
    archivo = open('historial_server.log','a')
    archivo.write(f"\nFecha: {fecha}, Opción: {opcion}, Cliente %s:%d" %(address))
    archivo.close()

def traerTicketsPorCantidad(lista, sock, cantidad):
    cantidad_integer = int(cantidad)
    #for x in range(cantidad_integer):
    for ticket in lista[0:cantidad_integer]:
        #tickets_objeto = json.dumps(lista, cls=MyEncoder)
        #sock.send(str(tickets_objeto).encode()) #manda lista al cliente
        ticket_objeto = json.dumps(ticket,cls=MyEncoder)
        sock.send(ticket_objeto.encode()) #manda los tickets de la base de datos
    #return ticket_objeto
try:
    while True:
            clientsocket, addr = serversocket.accept()
            print("\nObteniendo conexion desde %s:%d\n" % (addr[0],addr[1]))
            #th = threading.Thread(target=th_server, args=(clientsocket, addr))
            #th.start()
            ThreadCount += 1
            print('Thread Number: ' + str(ThreadCount), "\n")
            semaphore = threading.Semaphore(1)
            th = threading.Thread(target=th_server, args=(clientsocket, addr,semaphore)).start()
except KeyboardInterrupt:
        clientsocket.close()


