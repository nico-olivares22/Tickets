import socket
import threading
from funcions import *
import json,getopt,sys
(opcion, arg) = getopt.getopt(sys.argv[1:], 'p:')

for (op, ar) in opcion:
    if op == '-p':
        p = int(ar)
        print('Opcion -p exitosa!')

def th_server(sock,addr):
    print("Iniciando thread...\n")
    #print('Cliente %s:%s' % (addr))
    while True:
        opcion = sock.recv(1024)
        fecha = date.today() #fecha de operación
        print('Cliente %s:%s' % (addr[0], addr[1]))
        print("Opcion: " + opcion.decode()) #opción que viene desde el cliente
        print("Fecha: ", fecha) #imprimir fecha
        print("")
        if opcion.decode() == ('-i') or opcion.decode() == ('--insertar'):
            ticket = sock.recv(1024).decode()
            ticket_dict = json.loads(ticket)
            crearTicket(ticket_dict)
            print("Ticket creado por el Cliente %s:%s" %(addr), "\n")
            historial_server(fecha=fecha, opcion=opcion.decode(),address=addr)
        elif opcion.decode() == ('-l') or opcion.decode() == ('--listar'):
            ticket = sock.recv(1024).decode()
            tickets_objeto = json.loads(ticket)
            print("Cliente %s:%s ha listado los Tickets Disponibles" %(addr), "\n")
            historial_server(fecha=fecha, opcion=opcion.decode(),address=addr)

        elif opcion.decode() == ('-f') or opcion.decode() == ('--filtrar'):
            ticket = sock.recv(1024).decode()
            tickets_filter = json.loads(ticket)
            print("Cliente %s:%s ha filtrado los Tickets Disponibles" % (addr), "\n")
            historial_server(fecha=fecha, opcion=opcion.decode(),address=addr)
        elif opcion.decode() == ('-e') or opcion.decode() == ('--editar'):
            ticket = sock.recv(1024).decode()
            edit = json.loads(ticket)
            print("Cliente %s:%s ha editado un Ticket" % (addr), "\n")
            historial_server(fecha=fecha, opcion=opcion.decode(),address=addr)
        elif opcion.decode() == ('-c') or opcion.decode() == ('--cerrar'):
            print("Cliente %s:%s DESCONECTADO \n" %(addr))
            historial_server(fecha=fecha, opcion=opcion.decode(),address=addr)
            break

        else:
            print('\nOpcion invalida!\n')

#serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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

try:
    while True:
            clientsocket, addr = serversocket.accept()
            print("\nObteniendo conexion desde %s:%d\n" % (addr[0],addr[1]))
            th = threading.Thread(target=th_server, args=(clientsocket, addr))
            th.start()
            ThreadCount += 1
            print('Thread Number: ' + str(ThreadCount), "\n")
except KeyboardInterrupt:
        clientsocket.close()


