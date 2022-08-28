import mysql.connector

config = {
    'user': 'root',
    'password': 'Whoami*62303161',
    'host': 'localhost',
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
