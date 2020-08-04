from sqlalchemy import String, Integer, Column, DateTime, MetaData, Date
import json
from db_config import Base


class Ticket(Base):
    """
    Clase Ticket con sus Atributos los cuales se guardan en la Base de Datos.
    """
    __tablename__ = "tickets"
    ticket_Id = Column(Integer, primary_key=True)  # clave primaria
    title = Column(String(45), nullable=False)
    author = Column(String(45), nullable=False)
    description = Column(String(300), nullable=False)
    status = Column(String(45), nullable=False)
    date = Column(Date, nullable=False)

    def __repr__(self):
        """
        Esta función devuelve una cadena que contiene una representación imprimible de un objeto.
        Returns: la cadena
        """
        return '<Ticket: %r %r %r %r %r %r>' % (self.ticket_Id,self.title, self.author,self.description, self.status, self.date)

    def __init__(self, title, author, description, status, date):
        """
        Constructor de la Clase Ticket.
        Args:
            title: título del Ticket
            author: autor del Ticket
            description: Descripción del Ticket
            status: Estado del Ticket
            date: Fecha del Ticket
        """
        self.title = title
        self.author = author
        self.description = description
        self.status = status
        self.date = date

    # Convertir objeto Ticket  en JSON
    def toJSON(self):
        """
        Función que se encarga de convertir un objeto ticket a Json.
        Returns: ticket_json que es un diccionario

        """
        ticket_json = {
            'ticket_Id':self.ticket_Id,
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'status': self.status,
            'date': str(self.date)
        }
        return ticket_json

class MyEncoder(json.JSONEncoder):
    """
    Serializador para solucionar el error de Object type Ticket no es Serializable, dado que Json no sabe como serializar
    un objeto de tipo Ticket.
    """
    def default(self, obj):
        if isinstance(obj, Ticket):
            return {"ticket_Id":obj.ticket_Id,"title":obj.title, "author":obj.author, "description": obj.description, "status":obj.status, "date": str(obj.date)}
        return json.JSONEncoder.default(self,obj)


#Creación de Tablas
Base.metadata.create_all()


