import json
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from model import Publisher,Shop,Book,Stock,Sale,create_tables,drop_tables

DCM = 'postgresql://postgres:'
engine = sq.create_engine(DCM)
Session = sessionmaker(bind=engine)
session = Session()

def set_data (table:object,data:dict):
    result = table(**data)
    session.add(result)
    session.commit()

def load_fixtures ():
    models = [Publisher,Shop,Book,Stock,Sale]
    fixtures = ''
    with open('fixtures.json','r') as f:
        fixtures = json.load(f)
    for i in fixtures:
        model =''
        data = i['fields']
        data['id'] = i['pk']
        for m in models:
            if i['model'] == m.__tablename__:
                model = m
                break
        set_data(model,data)

def print_data (value,param = Publisher.name):
    select = session.query(Publisher)
    select = select.join(Book, Publisher.id == Book.id_publisher)
    select = select.join(Stock, Book.id == Stock.id_book)
    select = select.join(Shop, Shop.id == Stock.id_shop)
    select = select.join(Sale, Stock.id == Sale.id_stock)
    select = select.filter(param == value)
    form = 'название книги | название магазина, в котором была куплена эта книга | стоимость покупки | дата покупки'
    select, = select.all()

    for book in select.book:
        for stock in book.stock:
            for sale in stock.sale:
                form = str (sale.id) +' ' + book.title + ' | ' + stock.shop.name + ' | ' + str(sale.price) + ' | ' + str(sale.date_sale)
                print(form)


if __name__ == '__main__':
    tables = [Publisher,Shop,Book,Stock,Sale]

    load_fixtures()
    print_data(1,Publisher.id)


