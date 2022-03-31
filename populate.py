
from tabnanny import check
from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import csv
import os

def populate(empresa):
    class Database(): # contem informações importantes para conexão e manípulação do banco
        def __init__(self):
            self.engine = create_engine(f'mysql+pymysql://{empresa.user}:{getattr(empresa, "pass")}@{empresa.host}:41890/{empresa.database_name}') # engine de conexão
            self.base = declarative_base() # base para criar modelos
            self.Session = sessionmaker(bind=self.engine)

    class Leads(Database().base):
        __table__ = Table('rdstation_leads', Database().base.metadata,
                        autoload=True, autoload_with=Database().engine)

    database = Database().Session()

    # open csv

    with open(f'./leads/{empresa.name_project}/rd-bild-leads-todos-os-contatos-da-base-de-leads.csv', 'r', encoding='utf-8') as csv_refer:
        reader = csv.reader(csv_refer)
        for row in reader:
            row = str(row)
            row = row.replace("[", "")
            row = row.replace("]", "")
            row = row.replace("'", "")
            check_leads = database.query(Leads).filter_by(leads=row).first()

            if check_leads == None:
                new_lead = Leads(leads=row)
                database.add(new_lead)
                database.commit()
                
    os.remove(rf'.\leads\{empresa.name_project}\rd-bild-leads-todos-os-contatos-da-base-de-leads.csv')
