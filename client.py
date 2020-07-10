import socket,sys,getopt,json
from funciones_cliente import *
from model import MyEncoder
from json import JSONDecodeError


def recibirTickets(client, cantidad):
    cantidad_integer = int(cantidad) #cantidad que ingresa el user
    tickets = []
    for x in range(cantidad_integer):  # va cantidad integer
        tickets.append(client.recv(1024).decode())
    print("Tickets Agregados: ", len(tickets))
    imprimirTickets(tickets)


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
    client.send(opcion.encode())
    if opcion in ['-i','--insertar']:
        ticket=ingresar_DatosTicket()
        ticket_obj = json.dumps(ticket)
        client.send(ticket_obj.encode())
    elif opcion in ['-l','--listar']:
        cantidad_tickets = client.recv(1024).decode()
        print("La cantidad de Tickets es: ", cantidad_tickets)
        cantidad = input("Ingrese la Cantidad de Tickets que quiere Traer: ") # el user introduce la cantidad que quiera traer
        try:
            client.send(cantidad.encode())  # se la manda al server
            recibirTickets(client, cantidad)
        except JSONDecodeError:
            print("Cantidad NO válida, no hay esa cantidad de tickets disponible ;)")
    elif opcion in ['-f','--filtrar']:
        filtarTickets(client)
        cantidad_recibida = client.recv(1024).decode()  # linea 1
        print("Cantidad Recibida: ", cantidad_recibida)  # linea 2
        cantidad = input("Ingrese la Cantidad de Tickets que quiere Traer: ") #linea 4
        client.send(cantidad.encode()) #linea 4
        #tickets = client.recv(6115).decode()
        #tickets_filtrados = json.loads(tickets)
        #imprimirTicketsFiltrados(tickets_filtrados)
        recibirTickets(client,cantidad)
    elif opcion in ['-e','--editar']:
        option = input("Ingrese ID del Ticket: ")
        client.send(option.encode()) #manda el id el cliente
        ticket = client.recv(1024).decode() #recibe el ticket
        ticket_editado = menu_editar(ticket)
        ticket_editado_json = json.dumps(ticket_editado)
        client.send(ticket_editado_json.encode())

    elif opcion in ['-c','--cerrar']:
        break

    else:
        print('\nOpcion invalida!\n')
        input('Apretar Enter...')

try:
    print("")
except KeyboardInterrupt:
    client.close()



