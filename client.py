from funciones_cliente import *
from funciones_server import verificar_ticketID

client = createSocketCliente() #se crear el socket del cliente
establecerConexion_Cliente(client) # se establece la conexión del cliente

while True:

    print("""\n
    \t\t\t *** Menu ***
    * -i/--insertar para Insertar un Ticket
    * -l/--listar para Listar los Tickets 
    * -f/--filtrar para Filtrar Tickets
    * -e/--editar para Editar un Ticket
    * -d/--despachar para Exportar Tickets 
    * -c/--cerrar para Cerrar el Cliente
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
        cantidad_recibida = client.recv(1024).decode()
        print("Cantidad Recibida: ", cantidad_recibida)
        verificar = verificar_Cantidad_Cliente(cantidad_recibida) #linea agregada para verificar cantidad
        if verificar == False:
            print("NO hay tickets con ese/esos argumentos para Filtrar")
            continue
        cantidad = input("Ingrese la Cantidad de Tickets que quiere Traer: ")
        while int(cantidad) > int(cantidad_recibida):
            cantidad = str(input("Ha Ingresado una Cantidad Mayor a la Disponible, Ingrese la Cantidad de Tickets que quiere Traer: "))
        client.send(cantidad.encode())
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
        cantidad_recibida = client.recv(1024).decode()
        print("Cantidad Recibida: ", cantidad_recibida)
        verificar = verificar_Cantidad_Cliente(cantidad_recibida)  # linea agregada para verificar cantidad
        if verificar == False:
            print("NO hay tickets con ese/esos argumentos para Exportar")
            continue
        cantidad = input("Ingrese la Cantidad de Tickets que quiere Exportar: ")
        while int(cantidad) > int(cantidad_recibida):
            cantidad = str(input("Ha Ingresado una Cantidad Mayor a la Disponible, Ingrese la Cantidad de Tickets que quiere Exportar: "))
        client.send(cantidad.encode())
        recibirTicketsDespachados(client, cantidad)

    elif opcion in ['-c','--cerrar']:
        break

    else:
        print('\nOpción Inválida!\n')
        input('Aprete Enter...')

client.close()
