from sqlalchemy_declarative import Person, Address
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pprint import pprint as p

engine = create_engine('sqlite:///example.db')

DBSession = sessionmaker()

session = DBSession(bind=engine)

print("Listing all people from db")

for person in session.query(Person).all():
    p(person.name)

print("\nListing only first person")

person  = session.query(Person).first()
p(person.name)


print('\nListing all addresses whose person field is pointing to the person object')

addrs = session.query(Address).filter(Address.person == person).all()

for adr in addrs:
    p(adr.post_code)

print('\nGetting only one result')

adr = addrs = session.query(Address).filter(Address.person == person).one()

print(adr.post_code)