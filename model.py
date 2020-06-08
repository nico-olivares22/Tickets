from sqlalchemy import String, Integer, Column, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Ticket(Base):
    __tablename__ = "tickets"
    ticket_Id = Column(Integer, primary_key=True)  # clave primaria
    title = Column(String(45), nullable=False)
    author = Column(String(45), nullable=False)
    description = Column(String(300), nullable=False)
    status = Column(String(45), nullable=False)
    date = Column(DateTime, nullable=False)

    def __repr(self):
        return '<Ticket: %r %r %r %r %r %r>' % (self.ticket_Id,self.title, self.author,self.description, self.status, self.date)

    def __init__(self, title, author, description, status, date):
        self.title = title
        self.author = author
        self.description = description
        self.status = status
        self.date = date
