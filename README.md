# 🏠 HDB Resales ETL Project
### A joint project by team of 4 including myself during my Junior Data Engineer bootcamp
### I am responsible for development of LOAD process.

## 📘 Overview
This project implements an **Extract–Transform–Load (ETL) pipeline** for Singapore HDB resale flat data.  
The pipeline automates the process of:
- Extracting raw resale data (CSV).
- Transforming and cleaning the dataset.
- Loading the processed data into a PostgreSQL database.
- Providing utilities for analysis and visualization.


## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone <repo-url>
cd HDB-Resales-ETL/src
```
### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3.Configure Environment Variable
Create a ```.env```file inside ```/src```:
```
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=hdb_resales
```

## ⚙️ Setup Instructions

### 1. Step-by-Step
- Create Database
```
python create_db.py
```
- Create Table
```
python create_table.py
```
- Place Raw Data
- Put raw CSV files into data/raw/.
- Run ETL
- Option A: Run each phase individually:
```
python etl_extract.py
python etl_transform.py
python etl_load.py
```
- Option B: Run full pipeline:
```
python hdb_etl_pipeline.py
```
## ✅ Verification
- Check row counts between source and target.
- Run sample queries in PostgreSQL to confirm data integrity.

## 🔧 Maintenance & Improvements
- Automate extraction via API.
- Add error handling and retry logic.
- Schedule pipeline with Airflow or Cron.

## 📎 Appendix
- Glossary: ETL = Extract, Transform, Load.
- References:
  - [PostgreSQL](https://www.postgresql.org/docs/)
  - [pandas](https://pandas.pydata.org/docs/)
  - [SQLAchemy](https://docs.sqlalchemy.org/en/20/)




