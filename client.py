import socket
import sys
import getopt
import datetime
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
    * -i/--insertar para insertar un Ticket
    * -l/--listar para listar los Tickets 
    * -f/--filtrar para filtrar Tickets
    * -e/--editar para editar un Ticket
    * -c/--cerrar para cerrar el cliente
    """)
    opcion = input("Opción: ")
    opts, args = getopt.getopt(opcion, "p:a:ilfec",['insertar','listar','filtrar','editar','cerrar'] )
    print(opcion)
    #opcion = input('Opcion: ').upper() linea que estaba
    client.send(opcion.encode())
    #for op in opcion:
    if opcion in ['-i','--insertar']:
        print("Ingrese datos del Ticket")
        title = input("Título del Ticket: ")
        author = input("Autor del Ticket: ")
        description = input("Descripción del Ticket: ")
        status = input("Estado del Ticket: ")
        ticket = {"title": title, "author": author, "description": description, "status": status}
        ticket_obj = json.dumps(ticket)
        client.send(ticket_obj.encode())

    elif opcion in ['-l','--listar']:
        tickets = listarTickets()
        tickets_objeto = json.dumps(tickets)
        client.send(tickets_objeto.encode())


    elif opcion in ['-f','--filtrar']:
        tickets = filtarTickets()
        tickets_filter = json.dumps(tickets)
        client.send((tickets_filter.encode()))

    elif opcion in ['-e','--editar']:
        option = input("Ingrese ID del Ticket: ")
        ticket_edit = editTicket(str(option))
        edit_obj = json.dumps(ticket_edit)
        client.send(edit_obj.encode())

    elif opcion in ['-c','--cerrar']:
        break

    else:
        print('\nOpcion invalida!\n')
        input('Apretar Enter...')

client.close()

