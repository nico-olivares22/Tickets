from model import *
from db_config import *


def crearTicket(title, author, description, status, date):
    ticket = Ticket(title=title, author=author, description=description, status=status, date=date)
    session.add(ticket)
    session.commit()
    return ticket
