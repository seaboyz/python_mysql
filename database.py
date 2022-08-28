import mysql.connector

config = {
    'user': 'root',
    'password': '*',
    'host': 'localhost',
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
