from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-base model for the "Programmer" table

class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)

# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

#create records on our Programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

gracer_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)
jakeline_martines = Programmer(
    first_name="Jakeline",
    last_name="Martines",
    gender="F",
    nationality="Brazilian",
    famous_for="Brazilian Programmer"
)

# Add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(gracer_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(jakeline_martines)

# commit our session to the database
# muito similiar quando damos o commit no terminal para o GitHub
# session.commit()


# updating a single record

#programmer = session.query(Programmer).filter_by(id=12).first()
#programmer.famous_for = "World President"

# programmer = session.query(Programmer).filter_by(id=37).first()
# programmer.id = 7

# commit our session to the database
#session.commit()

# Updating multiple records 
#people = session.query(Programmer)
#for person in people:
#    if person.gender == "F":
#        person.gender = "Female"
#    elif person.gender == "M":
#        person.gender = "Male"
#    else: 
#        print("Gender not defined")
#    session.commit()

# deleting a single record 
#fname = input('Enter first name: ') #fname armazena o nome que o usuario inserir
# lname = input('Enter last name: ')
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# session.query percorre pelos dados dos programadores e filtra o primeiro nome que esta na tabela se é igual ao nome guardado na variavel fname e first da o resultado da consulta.
# defensive programming

# ids_delete = [17, 28, 29, 30, 31, 32, 33, 7, 12]

# for id_delete in ids_delete:
#     programmer = session.query(Programmer).filter(Programmer.id == id_delete).first()
    
#     if programmer is not None:
#         print("Programmer found: ", programmer.id)
#         confirmation = input("Are you sure you want delete this record? (y/n)")
#         if confirmation.lower() == "y":
#             session.delete(programmer)
#             session.commit()
#             print("Programmer has been deleted")
#         else:
#             print("Programmer not deleted")
#     else:
#         print("Not record found")



# query the database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )