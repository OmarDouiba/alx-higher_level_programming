#!/usr/bin/python3
from sqlalchemy import create_engine, PrimaryKeyConstraint, UniqueConstraint,ForeignKeyConstraint
from sqlalchemy import Column, Integer, String, DateTime, Index, ForeignKey, Table, SmallInteger, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

engine = create_engine("mysql+mysqldb://root:@localhost:3306/blog")
Base = declarative_base()

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table, SmallInteger, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

engine = create_engine("mysql+mysqldb://root:@localhost:3306/blog")
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    address = Column(String(200), nullable=True)  # Add address column
    town = Column(String(100), nullable=True)      # Add town column
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    orders = relationship("Order", back_populates='customer')

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now)
    customer = relationship("Customer", back_populates='orders')
    line_items = relationship("OrderLine", back_populates='order')


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)
    order_lines = relationship("OrderLine", back_populates='item')

class OrderLine(Base):
    __tablename__ = 'order_lines'
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())
    item = relationship("Item", back_populates='order_lines')
    order = relationship("Order", back_populates='line_items')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example usage:
c1 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden')

item1 = Item(name="Laptop", cost_price=1000.0, selling_price=1200.0)

order1 = Order(customer=c1)

order_line1 = OrderLine(quantity=2, item=item1, order=order1)

session.add_all([c1, item1, order1, order_line1])
session.commit()
