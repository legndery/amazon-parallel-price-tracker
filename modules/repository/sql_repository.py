from datetime import datetime
from sqlalchemy.sql.expression import false
from modules.repository.repository import Repository

from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Report(Base):
  __tablename__ = 'report'
  id = Column(Integer, primary_key=True)
  asin = Column(String(255), nullable=False)
  url = Column(String(255), nullable=False)
  title = Column(String(255), nullable=False)
  seller = Column(String(255), nullable=False)
  merchant = Column(String(255), nullable=False)
  price = Column(Float, nullable=False)
  date = Column(DateTime, nullable=False)

class SqlRepository(Repository):
  def __init__(self, decl_base):
    super().__init__()
    self.engine = create_engine(self.make_file_name())
    self.up(decl_base)
    decl_base.metadata.bind = self.engine
    DBSession = sessionmaker(bind=self.engine)
    self.session = DBSession()
  def make_file_name(self):
    return f'sqlite:///reports/sqlite/reports.db'
  def up(self, decl_base):
    decl_base.metadata.create_all(self.engine)
  def get_last_product(self, product_id):
    product= self.session.query(Report).filter(Report.asin == product_id).order_by(Report.date.desc()).limit(1).all()
    ret_val = {}
    if len(product) > 0:
      ret_val = product[0].__dict__
    print(ret_val)
    return ret_val
  def append_product(self, product):
    product['date'] = datetime.strptime(product['date'], "%d/%m/%Y %H:%M:%S")
    try:
      new_report = Report(**product)
      self.session.add(new_report)
      self.session.commit()
    except Exception as e:
      print(e)
  def get_price(self, product_id):
    try:
      price_list = self.session.query(Report).filter(Report.asin == product_id).order_by(Report.date.asc()).all()
      return [p.__dict__['price'] for p in price_list]
    except Exception as e:
      print(e)

if __name__ == "__main__":
  print(SqlRepository(Base).get_price('B07YFF3JCN'))