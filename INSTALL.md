# INSTRUCCIONES PARA LANZAR E INSTALAR LA APLICACIÓN
    Los siguientes pasos para lanzar la Aplicación son para el Sistema Operativo Linux.
    Antes de hacer los siguientes pasos hay que tener instalado python3, pip3, virtualenv y MySQL. 
    Para instalar python3 ejecute: 
    $ sudo apt-get update
    $ sudo apt-get install python3
    Para instalar pip3 ejecute:
    $ sudo apt-get install python3-pip
    Para instalar virtualenv ejecute:
    $ sudo pip3 install virtualenv
    Para instalar MySQL dirigase al siguiente link que contiene los pasos detallados de la instalación:
    https://www.digitalocean.com/community/tutorials/como-instalar-mysql-en-ubuntu-18-04-es
    Pasos:
    1) Crear un Entorno virtual: para crear un entorno virtual debe dirigirse a un directorio particular y ejecutar virtualenv nombre_de_tu_entorno -p python3.
    2) Activar o Desactivar el Entorno: Para activar el Entorno virtual dirigase al directorio donde creo el entorno y ejecute source nombre_entorno_virtual/bin/activate y para desactivarlo 
    ejecute deactivate.
    3) Ejecutar el archivo requirements.txt: Con el Entorno activado ejecutar 
    pip3 install -r requirements.txt.
    4) Crear Base de Datos: Dirigase al MySQL Workbench y cree una base de datos con el nombre que desee.
    5) Generar Archivo .env para para acceder a la Base de Datos: Una vez que estén los paquetes
    instalados tiene que ir al directorio de su entorno, activarlo y crear un archivo llamado .env con los siguientes datos:
        DB_USER = usuario de la base de datos.
        DB_PASSWORD = contraseña de la base de datos.
        DB_NAME = nombre de la base de datos que generó en el paso anterior.
    6) Clonar Repositorio: Ya con todo configurado e instalado tiene que clonar los archivos 
    del repositorio dentro del entorno virtual.
        Para clonar tiene que hacer git clone https://gitlab.com/Nicolas_Olivares22/sistema-de-tickets.git en el directorio de su entorno virtual activado.
    7) Lanzar aplicación: Para lanzar la aplicacion tiene que abrir dos terminales como mínimo y ejecutar el servidor primero de la siguiente manera: python3 server.py -p 3030 por ejemplo y para ejecutar 
    un cliente en la otra terminal es python3 client -p 3030 -a localhost.
    8) Realizar Operaciones: Ya con el cliente funcionando puede hacer operaciones explicadas 
    detalladamente en el README.md
    
    
    


