from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_declarative import Address, Base, Person

engine = create_engine('sqlite:///example.db')

DBSession = sessionmaker(bind=engine)

session = DBSession()

new_person = Person(name='new_person')
session.add(new_person)
session.commit()

new_address = Address(post_code='0000', person=new_person)
session.add(new_address)
session.commit()