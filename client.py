from funciones_cliente import *
from funciones_server import verificar_ticketID

client = createSocketCliente()
establecerConexion_Cliente(client)

while True:

    print("""\n
    \t\t\t *** Menu ***
    * -i/--insertar para insertar un Ticket
    * -l/--listar para listar los Tickets 
    * -f/--filtrar para filtrar Tickets
    * -e/--editar para editar un Ticket
    * -d/--despachar para exportar tickets 
    * -c/--cerrar para cerrar el cliente
    """)
    opcion = input("Opción: ")
    opts, args = getopt.getopt(opcion, "p:a:ilfedc",['insertar','listar','filtrar','editar','despachar','cerrar'] )
    client.send(opcion.encode())
    if opcion in ['-i','--insertar']:
        ticket = ingresar_DatosTicket()
        ticket_obj = json.dumps(ticket)
        client.send(ticket_obj.encode())

    elif opcion in ['-l','--listar']:
        cantidad_tickets = client.recv(1024).decode()
        print("La cantidad de Tickets es: ", cantidad_tickets)
        cantidad = input("Ingrese la Cantidad de Tickets que quiere Traer: ") # el user introduce la cantidad que quiera traer
        try:
            while int(cantidad) > int(cantidad_tickets):
                cantidad = str(input("Ha Ingresado una Cantidad Mayor a la Disponible, Ingrese Nuevamente: "))
        except ValueError:
            cantidad = str(input("Ha INGRESADO un Carácter, Ingrese la Cantidad de Tickets que quiere Traer: "))
        client.send(cantidad.encode())
        recibirTickets(client, cantidad)

    elif opcion in ['-f','--filtrar']:
        filtarTickets(client)
        cantidad_recibida = client.recv(1024).decode()  # linea 1
        print("Cantidad Recibida: ", cantidad_recibida)
        verificar = verificar_Cantidad_Cliente(cantidad_recibida) #linea agregada para verificar cantidad
        if verificar == False:
            print("NO hay tickets con ese/esos argumentos para Filtrar")
            continue
        cantidad = input("Ingrese la Cantidad de Tickets que quiere Traer: ")
        while int(cantidad) > int(cantidad_recibida):
            cantidad = str(input("Ingrese la Cantidad de Tickets que quiere Traer: "))
        client.send(cantidad.encode())  # linea 4
        recibirTickets(client, cantidad)

    elif opcion in ['-e','--editar']:
        ticket_ID = input("Ingrese ID del Ticket: ")
        verificar = verificar_ticketID(ticket_ID)
        client.send(ticket_ID.encode())  # manda el id el cliente
        if verificar == False:
            print("NO existe un TICKET con el ID ingresado")
            continue
        ticket = client.recv(1024).decode()  # recibe el ticket
        ticket_editado = menu_editar(ticket)
        ticket_editado_json = json.dumps(ticket_editado)
        client.send(ticket_editado_json.encode())

    elif opcion in ['-d', '--despachar']:
        despacharTicketsCliente(client)
        cantidad_recibida = client.recv(1024).decode()  # linea 1
        print("Cantidad Recibida: ", cantidad_recibida)  # linea 2
        verificar = verificar_Cantidad_Cliente(cantidad_recibida)  # linea agregada para verificar cantidad
        if verificar == False:
            print("NO hay tickets con ese/esos argumentos para Exportar")
            continue
        cantidad = input("Ingrese la Cantidad de Tickets que quiere Exportar: ")  # linea 4
        while int(cantidad) > int(cantidad_recibida):
            cantidad = str(input("Ingrese la Cantidad de Tickets que quiere Traer: "))
        client.send(cantidad.encode())  # linea 4
        recibirTicketsDespachados(client, cantidad)

    elif opcion in ['-c','--cerrar']:
        break
    else:
        print('\nOpcion invalida!\n')
        input('Apretar Enter...')
try:
    print("")
except KeyboardInterrupt:
    client.close()