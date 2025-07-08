from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
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

meta.create_all(engine)

conn = engine.connect()

select_statement = people.select().where(people.c.name == "John")
result = conn.execute(select_statement)

for row in result.fetchall():
    print(row)

update_statement = people.update().where(people.c.name == "John").values(age=31)
result = conn.execute(update_statement)
conn.commit()
