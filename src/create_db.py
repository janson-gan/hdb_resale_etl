from sqlalchemy_utils import database_exists, create_database
from connection import get_engine, DB_NAME
from config import logging

engine = get_engine()

try:
    if not database_exists(engine.url):
        create_database(engine.url)
        logging.info(f"{DB_NAME} database created successfully!")
    else:
        logging.info(f"{DB_NAME} database already exists!")
except Exception as e:
    logging.error(f"Fail to create database! Error: {e}")

engine.dispose()
logging.info("Database disconnected successfully.")