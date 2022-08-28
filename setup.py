import mysql.connector
from database import cursor

DB_NAME = 'test'


def create_db():
    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS {DB_NAME} DEFAULT CHARACTER SET 'utf8'"
    )
    print(f"Database {DB_NAME} created")


create_db()