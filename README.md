# SISTEMA DE TICKETS
    Es un software hecho en python y SqlAlchemy en la terminal de Linux para la Administración de Tickets.
## Contenido
    Este sistema tiene tres ramas: una se llama nicodev en la cual está todo el trabajo que ha requerido 
    el proyecto, y la otra rama es developer que es una rama auxliar que contiene las copias de segurida de nicodev. La última rama es la master que tiene el proyecto ya finalizado.
## Uso Básico del Proyecto
    El uso principal del proyecto es el intercambio de infromacion entre el servidor y los clientes.
    Las operaciones que pueden realizar los clientes mientras el servidor escucha son:
        -i/--insertar: operación permite insertar un nuevo Ticket.
        -l/--listar: operación que permite listar todos los Tickets.
        -f/--filtrar: operación que permite filtrar los Tickets por autor, estado y fecha. Los filtros 
        pueden ser simultáneos.
        -e/--editar: operación que permite modificar un Ticket en particular, se puede modficar el Título, Estado y Descripción del Ticket unicamente.
        -d/--despachar: operación que permite exportar Tickets mediante un filtro a un archivo CSV 
        comprimido.


