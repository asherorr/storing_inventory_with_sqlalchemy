from sqlalchemy import (create_engine, Column,
                        Integer, String, Date)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




engine = create_engine('sqlite:///inventory.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True)
    product_name = Column("Product Name", String)
    product_price = Column("Product Price", Integer)
    product_quantity = Column("Product Quantity", Integer)
    date_updated = Column("Date Updated", Date)
    
    def __repr__(self):
        return f'Name: {self.product_name}, Quantity: {self.product_quantity}, Price: {self.product_price}, Date Updated: {self.date_updated}'


if __name__ == "__main__":
    Base.metadata.create_all(engine)