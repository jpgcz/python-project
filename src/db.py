from pony.orm import Database
from os import getenv

def setup_db():
    app_db = Database()
    app_db.bind(
        provider='postgres',
        user=getenv("DB_USER"),
        password=getenv("DB_PASSWORD"),
        host=getenv("DB_HOST"),
        port=getenv("DB_PORT"),
        database=getenv("DB_NAME"),
        sslmode='require'
    )

    return app_db


app_db = setup_db()
