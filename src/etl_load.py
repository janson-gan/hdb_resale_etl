import pandas as pd
from pathlib import Path
from sqlalchemy import text
from tqdm import tqdm
from connection import get_engine, DB_NAME
from schema import resales_prices
from config import logging

# init the connection to postgres database
engine = get_engine()

def run(data_frame):
    # connection to the database
    try:
        with engine.connect() as connection:
            # verify the connection by selecting the database version
            version = connection.execute(text("SELECT version();")).fetchone()
            logging.info(f"Successfully connected to {DB_NAME} database, version: {version[0]}")
    except Exception as e:
        logging.error(f'Fail to connect database. Error: {e}')

    # get the absolute path for current script directory 
    project_root = Path(__file__).resolve().parent.parent
    # join target data path to with project root
    file_path = project_root/data_frame

    # extract processed data to dataframe format
    df = pd.read_csv(file_path)
    logging.info(f"Dataframe loaded with {len(df)} rows.")
    # get the table columns name
    table_columns = [col.name for col in resales_prices.columns]
    # display progress bar while loading csv data into database table
    try:
        with tqdm(total=len(df), desc="Loading data") as pbar:
            # Read the csv file in chunk of 5000 rows, to avoid memory lost 
            for chunk in pd.read_csv(file_path, chunksize=5000):
                # match csv columns to table schema
                chunk = chunk[table_columns]
                # set the chunks of data to sql table
                chunk.to_sql(
                    resales_prices.name,        # database table name
                    engine,                     # database connection
                    if_exists = "append",       # insert new rows without overwriting
                    index=False                 # omit dataframe index insert into database table
                )
                # update the number of rows just inserted
                pbar.update(len(chunk))
        logging.info(f"Successfully loaded {len(df)} rows into {DB_NAME} database.")
    except Exception as e:
        logging.error(f"Fail to load data into database! Error: {e}")

    # validate database table row count to processed data row count
    table_row = pd.read_sql(f"SELECT COUNT(*) FROM {resales_prices.name}", engine)
    row_count = table_row.iloc[0, 0]
    logging.info(f"Processed data: {len(df)} rows, resales_prices table: {row_count} rows.")

    # close database connection
    engine.dispose()
    logging.info("Database disconnected successfully.")
