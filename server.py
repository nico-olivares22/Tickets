import socket
import threading
from funcions import *

(opcion, arg) = getopt.getopt(sys.argv[1:], 'p:')

for (op, ar) in opcion:
    if op == '-p':
        p = int(ar)
        print('Opcion -p exitosa!')


def th_server(sock):
    print("Iniciando thread...\n")
    print('Cliente %s:%s' % (addr[0], addr[1]))
    while True:
        opcion = sock.recv(1024)
        fecha = date.today() #fecha de operación
        #print('Cliente %s:%s' % (addr[0], addr[1]))
        print("Opcion: " + opcion.decode()) #opción que viene desde el cliente
        print("Fecha: ", fecha) #imprimir fecha
        print("")
        historial_server(fecha=fecha, opcion=opcion.decode())
        if opcion.decode() == ('-i') or opcion.decode() == ('--insertar'):
            ticket = sock.recv(1024).decode()
            ticket_dict = json.loads(ticket)
            crearTicket(ticket_dict)
            print("Ticket creado por el Cliente %s:%s" %(addr[0],addr[1]), "\n")

        elif opcion.decode() == ('-l') or opcion.decode() == ('--listar'):
            ticket = sock.recv(1024).decode()
            tickets_objeto = json.loads(ticket)
            print("Cliente %s:%s ha listado los Tickets Disponibles" %(addr[0],addr[1]), "\n")


        elif opcion.decode() == ('-f') or opcion.decode() == ('--filtrar'):
            ticket = sock.recv(1024).decode()
            tickets_filter = json.loads(ticket)
            print("Cliente %s:%s ha filtrado los Tickets Disponibles" % (addr[0], addr[1]), "\n")

        elif opcion.decode() == ('-e') or opcion.decode() == ('--editar'):
            ticket = sock.recv(1024).decode()
            edit = json.loads(ticket)
            print("Cliente %s:%s ha editado un Ticket" % (addr[0], addr[1]), "\n")

        elif opcion.decode() == ('-c') or opcion.decode() == ('--cerrar'):
            print("Cliente %s:%s DESCONECTADO \n" %(addr[0],addr[1]))
            break

        else:
            print('\nOpcion invalida!\n')

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
port = p

serversocket.bind((host, port))
serversocket.listen(5)

def historial_server(fecha,opcion):
    archivo = open('historial.log','a')
    archivo.write(f"\nFecha: {fecha},Opción: {opcion},IP del Cliente %s:%d\n" % (addr[0],addr[1]))
    archivo.close()

try:
    while True:
        clientsocket, addr = serversocket.accept()
        print("\nObteniendo conexion desde %s:%d\n" % addr)
        th = threading.Thread(target=th_server, args=(clientsocket,))
        th.start()
except KeyboardInterrupt:
    clientsocket.close()



