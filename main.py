from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost:5432/{os.getenv('DB_NAME')}",
    echo=True,
)

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    things = relationship("Thing", back_populates="person")


class Thing(Base):
    __tablename__ = "things"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    owner = Column(Integer, ForeignKey("people.id"))

    person = relationship("Person", back_populates="things")


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_person = Person(name="Charlie", age=70)
session.add(new_person)
session.flush()
new_thing = Thing(description="A book", price=10.0, owner=new_person.id)
session.add(new_thing)

session.commit()

print(new_person.things)
print(new_thing.person)
