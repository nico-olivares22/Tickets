from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base
from os import getenv
from dotenv import load_dotenv

load_dotenv() #Pasea el archivo .env y luego carga las variables de entorno
#Configuración Base de Datos
engine = create_engine(f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@localhost/{getenv('DB_NAME')}")
#Creación de Tablas
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine) #Se obtiene las sesiones de BD
session = Session() #Después de crear la factoría, objeto Session, hay que hacer llamadas a la misma para obtener las sesiones, objeto session.

