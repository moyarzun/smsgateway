### Configuration
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

### Class
class Restaurant(Base):
    # syntax: __tablename__ = 'some_table'
    __tablename__ = 'restaurant'

    ### Mapper
    #syntax: columnName = Column(attributes, ...)
    id= Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)


class MenuItem(Base):
    # syntax: __tablename__ = 'some_table'
    __tablename__ = 'menu_item'

    ### Mapper
    #syntax: columnName = Column(attributes, ...)
    id = Column(Integer, primary_key = True)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    name = Column(String(80), nullable=False)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))

    @property
    def serialize(self):
        return{
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }

### Configuration cont'd
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
