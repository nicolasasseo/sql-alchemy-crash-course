# SQLAlchemy Crash Course – Practice Project

This project is a collection of scripts created while following a tutorial to learn SQLAlchemy, the popular Python SQL toolkit and Object Relational Mapper. The code demonstrates both the Core and ORM APIs, as well as integration with pandas.

## Project Structure

- **basics.py**  
  Demonstrates basic usage of SQLAlchemy Core with SQLite.

  - Creates a simple `people` table.
  - Inserts a row using raw SQL.
  - Shows how to connect and execute statements.

- **core.py**  
  Explores more advanced SQLAlchemy Core features with PostgreSQL.

  - Defines `people` and `things` tables with relationships.
  - Performs bulk inserts.
  - Demonstrates joins and group-by queries.
  - Uses environment variables for database credentials.

- **main.py**  
  Introduces SQLAlchemy ORM (Object Relational Mapper) with PostgreSQL.

  - Defines `Person` and `Thing` classes mapped to tables.
  - Demonstrates one-to-many relationships.
  - Shows how to add and query related objects using the ORM.

- **pandastodb.py**  
  Shows how to use pandas with SQLAlchemy for data analysis and manipulation.

  - Inserts a DataFrame into the `people` table in PostgreSQL.
  - Reads the table back into a DataFrame.

- **test.db**  
  SQLite database file used by `basics.py`.

## Getting Started

1. **Install dependencies**  
   You’ll need Python 3, SQLAlchemy, pandas, python-dotenv, and a PostgreSQL server.  
   Install with:

   ```
   pip install sqlalchemy pandas python-dotenv psycopg2
   ```

2. **Set up your environment variables**  
   Create a `.env` file in the project root with:

   ```
   DB_USER=your_postgres_user
   DB_PASSWORD=your_postgres_password
   DB_NAME=your_database_name
   ```

3. **Run the scripts**
   - For SQLite examples:
     ```
     python basics.py
     ```
   - For PostgreSQL examples:
     ```
     python core.py
     python main.py
     python pandastodb.py
     ```

## Notes

- The scripts are meant for learning and experimentation.
- Make sure your PostgreSQL server is running and the credentials in `.env` are correct.
- The code demonstrates both the Core (SQL-like) and ORM (object-oriented) approaches in SQLAlchemy.
- You can explore and modify the scripts to deepen your understanding.

---

Happy learning!
