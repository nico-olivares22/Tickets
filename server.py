from db_config import *
import socket
import sys
import threading
import json
import getopt
from funcions import *
from model import *

(opcion, arg) = getopt.getopt(sys.argv[1:], 'p:')

for (op, ar) in opcion:
    if op == '-p':
        p = int(ar)
        print('Opcion -p exitosa!')


def th_server(sock):
    print("Iniciando thread...\n")
    while True:

        opcion = sock.recv(1024)
        print('Cliente %s:%s' % (addr[0], addr[1]))
        print("Opcion: " + opcion.decode() + '\n')

        if opcion.decode() == 'INSERTAR':
            ticket=sock.recv(1024).decode()
            ticket_dict=json.loads(ticket)
            print(type(ticket_dict))
            print(ticket_dict)
            crearTicket(ticket_dict)



        elif (opcion.decode() == 'LISTAR'):
            print("HOLA AMIGO")

        elif (opcion.decode() == 'LEER'):
            fd = open(archivo, 'r')
            print('\nEnviando archivo al cliente: ' + archivo + '\n')
            contenido = fd.read()
            sock.sendall(contenido.encode())
            fd.close()

        elif (opcion.decode() == 'CERRAR'):
            fd.close()
            break

        else:
            print('\nOpcion invalida!\n')


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
port = p

serversocket.bind((host, port))

serversocket.listen(5)

while True:
    clientsocket, addr = serversocket.accept()
    print("\nObteniendo conexion desde %s:%s\n" % (addr[0], addr[1]))
    th = threading.Thread(target=th_server, args=(clientsocket,))
    th.start()
clientsocket.close()
