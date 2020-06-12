import socket
import sys
import getopt
from datetime import datetime
import json
from funcions import *
import datetime

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
    - LISTAR
    - FILTRAR
    - EDITAR
    - CERRAR
    """)

    opcion = input('Opcion: ').upper()

    client.send(opcion.encode())

    if (opcion == 'INSERTAR'):
        print("Ingrese datos del Ticket")
        title = input("Título del Ticket: ")
        author = input("Autor del Ticket: ")
        description = input("Descripción del Ticket: ")
        status = input("Estado del Ticket: ")
        ticket = {"title": title, "author": author, "description": description, "status": status}
        ticket_obj = json.dumps(ticket)
        client.send(ticket_obj.encode())

    elif (opcion == 'LISTAR'):
        tickets = listarTickets()
        tickets_objeto = json.dumps(tickets)
        client.send(tickets_objeto.encode())


    elif (opcion == 'FILTRAR'):
        option= input("Opción por filtrar: ")
        tickets= filtrarByAuthor()
        tickets_filter = json.dumps(tickets)
        client.send((tickets_filter.encode()))

    elif (opcion == 'EDITAR'):
        print("Editar")
    elif (opcion == 'CERRAR'):
        break

    else:
        print('\nOpcion invalida!\n')
        input('Apretar Enter...')

client.close()
