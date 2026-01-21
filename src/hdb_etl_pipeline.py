import logging
import etl_extract
import etl_transform
import etl_load

def main():
    logging.info("Starting ETL pipeline...Extracting...")
    df_raw = etl_extract.run()
    logging.info("Starting transforming...")
    df_transformed = etl_transform.run(df_raw)
    logging.info("Starting loading...")
    etl_load.run(df_transformed)

# run the code only when it is executed directly on this file
# Do nothing when the file is imported to other file
if __name__ == "__main__":
    main()