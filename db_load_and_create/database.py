import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

hostanme = os.getenv('HOSTNAME')
database = os.getenv('DATABASE')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
port = os.getenv('PORT')

try:
    connection = psycopg2.connect(
        host = hostanme,
        dbname = database,
        user = username,
        password = password,
        port = port
    )

    cursor = connection.cursor()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)