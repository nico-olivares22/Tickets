from sqlalchemy import String, Integer, Column, DateTime, MetaData, Date
import json
from db_config import Base


class Ticket(Base):
    __tablename__ = "tickets"
    ticket_Id = Column(Integer, primary_key=True)  # clave primaria
    title = Column(String(45), nullable=False)
    author = Column(String(45), nullable=False)
    description = Column(String(300), nullable=False)
    status = Column(String(45), nullable=False)
    date = Column(Date, nullable=False)

    def __repr__(self):
        return '<Ticket: %r %r %r %r %r %r>' % (self.ticket_Id,self.title, self.author,self.description, self.status, self.date)

    def __init__(self, title, author, description, status, date):
        self.title = title
        self.author = author
        self.description = description
        self.status = status
        self.date = date

    # Convertir objeto Ticket  en JSON
    def toJSON(self):
        ticket_json = {
            'ticket_Id':self.ticket_Id,
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'status': self.status,
            'date': str(self.date)
        }
        return ticket_json


    # Convertir JSON a objeto
    @staticmethod
    def desde_json(ticket_json):  # clave valor
        ticket_Id = ticket_json.ticket_Id
        title = ticket_json.title
        author = ticket_json.author
        description = ticket_json.description
        status = ticket_json.status
        date = ticket_json.date
        return Ticket(title=title,author=author,description=description,status=status,date=date)

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Ticket):
            return {"ticket_Id":obj.ticket_Id,"title":obj.title, "author":obj.author, "description": obj.description, "status":obj.status, "date": str(obj.date)}
        return json.JSONEncoder.default(self,obj)


#Creación de Tablas
Base.metadata.create_all()


