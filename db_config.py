from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
load_dotenv() #Pasea el archivo .env y luego carga las variables de entorno.
#Configuración Base de Datos
engine = create_engine(f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@localhost/{getenv('DB_NAME')}") #El engine es el punto de entrada a la base de datos, es decir, el que permite a SQLAlchemy comunicarse con esta.
Session = sessionmaker(bind = engine) #Se obtiene las sesiones de BD.
session = Session() #Después de crear la factoría, objeto Session, hay que hacer llamadas a la misma para obtener las sesiones, objeto session.
Base = declarative_base(bind=engine) #Esta clase será de la que hereden todos los modelos y tiene la capacidad de realizar el mapeo correspondiente a partir de la metainformación.
#Una sesión viene a ser como una transacción, es decir, un conjunto de operaciones de base de datos que, bien se ejecutan todas de forma atómica.
