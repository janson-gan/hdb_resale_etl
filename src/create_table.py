from config import logging
from sqlalchemy.schema import CreateTable
from connection import get_engine, DB_NAME
from schema import resales_prices

# init the connection to postgres database
engine = get_engine()

# connection to postgres databse
try:
    with engine.connect() as connection:
        # execute the create table query
        create_table = connection.execute(CreateTable(resales_prices))
        # Save changes permanently in the database
        connection.commit()
        logging.info(f"Table created successfully into {DB_NAME} database!")
except Exception as e:
    logging.error(f'Fail to create table in {DB_NAME} database. Error: {e}')

# close connection
engine.dispose()
logging.info("Database disconnected successfully.")