import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()

class Publisher (Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key = True)
    name = sq.Column(sq.String(length=40), unique = True)

class Shop (Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key = True)
    name = sq.Column(sq.String(length=40), unique = True)


class Book (Base):
    __tablename__ = 'book'

    id = sq.Column(sq.INTEGER,primary_key = True)
    title = sq.Column(sq.String(length=40))
    id_publisher = sq.Column(sq.ForeignKey(Publisher.id))

    publisher = relationship(Publisher, backref = 'book')

class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.INTEGER, primary_key = True)
    id_book = sq.Column(sq.ForeignKey(Book.id))
    id_shop = sq.Column(sq.ForeignKey(Shop.id))
    count = sq.Column(sq.INTEGER)

    book = relationship(Book, backref = 'stock')
    shop = relationship(Shop, backref = 'stock')


class Sale (Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer,primary_key = True)
    price = sq.Column(sq.Float)
    date_sale = sq.Column(sq.DateTime)
    id_stock = sq.Column(sq.ForeignKey(Stock.id))
    count = sq.Column(sq.Integer)

    stock = relationship(Stock, backref = 'sale')

def create_tables(engine):
    Base.metadata.create_all(engine)

def drop_tables (engine):
    Base.metadata.drop_all(engine)