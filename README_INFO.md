# DECISIONES PRINCIPALES DEL DISEÑO DEL PROYECTO
* BASE DE DATOS RELACIONAL: Elegí MySQL porque siempre he trabajado con este tipo de Almacenamiento y no conozco ni he trabajado con Base de Datos NoSQL.
* SQLAlchemy: Es el mapeador relacional de objetos para el lenguaje de programacion Python.
* socket.AF_INET, socket.SOCK_STREAM: Es lo que permite comunicar al servidor con el cliente o con los clientes. AF_INTET se refiere a la familia de direcciones IPV4, mientras que SOCK_STREAM significa que es un socket TCP (Protocolo de Control de Transmisión).
* getopt: Módulo utilizado para hacer operaciones mediante comando. Cada comando tiene una letra en particular y una palabra en particular para una determinada operación. 
* json: Módulo utilizado para el intercambio de Datos entre el servidor y el cliente, decídi usar json porque me pareció más sencillo de entender que pickle (módulo de Python).
* multiprocessing: Usé multiprocessing para largar el proceso pararelo a la ejecución del sistema cuando el cliente hace la operación de exportar Tickets.
* threading: Usé threading para que el servidor lance un hilo por cada cliente que se conecte y así el servidor trata de manera independiente a cada cliente.
    
    
    
    


