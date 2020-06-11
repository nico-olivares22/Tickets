import socket
import sys
import getopt
from datetime import datetime
import json
from funcions import listarTickets
from model import *
(opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:')

for (op, ar) in opt:
    if op == '-a':
        a = str(ar)
    elif op == '-p':
        p = int(ar)
        print('Opcion -p exitosa!')

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Fallo al crear el socket!')
    sys.exit()

print('Socket Creado!')

host = a
port = p

client.connect((host, port))

print('Socket conectado al host', host, 'en el puerto', port)

while True:

    print("""\n
    \t\t\t *** Menu ***
    - INSERTAR
    - AGREGAR
    - LEER
    - CERRAR
    """)

    opcion = input('Opcion: ').upper()

    client.sendto(opcion.encode(), (host, port))

    if (opcion == 'INSERTAR'):
        print("Ingrese datos del Ticket")
        title = input("Título del Ticket: ")
        author = input("Autor del Ticket: ")
        description = input("Descripción del Ticket: ")
        status = input("Estado del Ticket: ")
        #date = datetime.now()
        ticket = {"title": title,"author": author,"description": description,"status": status}#,"date": str(date)}
        ticket_obj = json.dumps(ticket)
        client.send(ticket_obj.encode())
        print(type(ticket))

    elif (opcion == 'LISTAR'):
        listarTickets()


    elif (opcion == 'LEER'):
        contenido = client.recv(1024).decode()
        print('\nArchivo: ' + archivo + '\n')
        print(contenido)
        input('Apretar Enter...')

    elif (opcion == 'CERRAR'):
        break

    else:
        print('\nOpcion invalida!\n')
        input('Apretar Enter...')

client.close()
