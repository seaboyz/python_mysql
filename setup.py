from mysql.connector import errorcode
import mysql.connector
from database import cursor
DB_NAME = 'test'

TABLES = {}

TABLES['logs'] = (
    "CREATE TABLE `logs` ("
    " `id` int(11) NOT NULL AUTO_INCREMENT,"
    " `text` varchar(250) NOT NULL,"
    " `user` varchar(250) NOT NULL,"
    " `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)


def create_db():
    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS {DB_NAME} DEFAULT CHARACTER SET 'utf8'"
    )
    print(f"Database {DB_NAME} created")


def create_tables():
    cursor.execute(f"USE {DB_NAME}")
    for name, ddl in TABLES.items():
        try:
            print(f"Creating table {name}")
            cursor.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print(f"Table {name} already exists")
            else:
                print(err.msg)
        else:
            print(f"Table {name} created")


create_db()
create_tables()
