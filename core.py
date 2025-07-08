from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    func,
)
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost:5432/{os.getenv('DB_NAME')}",
    echo=True,
)

meta = MetaData()
people = Table(
    "people",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer),
)

things = Table(
    "things",
    meta,
    Column("id", Integer, primary_key=True),
    Column("description", String, nullable=False),
    Column("price", Float),
    Column("owner", Integer, ForeignKey("people.id")),
)

meta.create_all(engine)

conn = engine.connect()

# select_statement = people.select().where(people.c.name == "John")
# result = conn.execute(select_statement)

# for row in result.fetchall():
#     print(row)

# update_statement = people.update().where(people.c.name == "John").values(age=31)
# result = conn.execute(update_statement)
# conn.commit()

insert_people = people.insert().values(
    [
        {"name": "John", "age": 30},
        {"name": "Jane", "age": 25},
        {"name": "Jim", "age": 35},
        {"name": "Jill", "age": 28},
        {"name": "Jack", "age": 32},
        {"name": "Jill", "age": 28},
    ]
)

insert_things = things.insert().values(
    [
        {"description": "laptop", "price": 1200.0, "owner": 1},
        {"description": "keyboard", "price": 100.0, "owner": 1},
        {"description": "mouse", "price": 50.0, "owner": 1},
        {"description": "sewing kit", "price": 40.0, "owner": 2},
        {"description": "chemistry kit", "price": 80.0, "owner": 4},
    ]
)

join_statement = people.outerjoin(things, people.c.id == things.c.owner)

select = (
    people.select()
    .with_only_columns(people.c.name, things.c.description)
    .select_from(join_statement)
)

result = conn.execute(select)
for row in result.fetchall():
    print(row)


group_statement = (
    things.select()
    .with_only_columns(things.c.owner, func.sum(things.c.price))
    .group_by(things.c.owner)
)

result = conn.execute(group_statement)
for row in result.fetchall():
    print(row)
