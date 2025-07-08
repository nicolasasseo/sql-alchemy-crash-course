from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost:5432/{os.getenv('DB_NAME')}",
    echo=True,
)

# df = pd.read_sql("SELECT * FROM people", con=engine)
# print(df)

newdata = pd.DataFrame({"name": ["Nico", "Nick"], "age": [25, 30]})
newdata.to_sql("people", con=engine, if_exists="append", index=False)

df = pd.read_sql("SELECT * FROM people", con=engine)
print(df)
