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

        if opcion.decode() == ('-i') or opcion.decode() == ('--insertar'):
            ticket = sock.recv(1024).decode()
            ticket_dict = json.loads(ticket)
            crearTicket(ticket_dict)

        elif opcion.decode() == ('-l') or opcion.decode() == ('--listar'):
            ticket = sock.recv(1024).decode()
            tickets_objeto = json.loads(ticket)


        elif opcion.decode() == ('-f') or opcion.decode() == ('--filtrar'):
            ticket = sock.recv(1024).decode()
            tickets_filter = json.loads(ticket)

        elif opcion.decode() == ('-e') or opcion.decode() == ('--editar'):
            ticket = sock.recv(1024).decode()
            edit = json.loads(ticket)


        elif opcion.decode() == ('-c') or opcion.decode() == ('--cerrar'):
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
