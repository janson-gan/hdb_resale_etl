# 🏠 HDB Resales ETL Project

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
### Install Dependencies
```
pip install -r requirements.txt
```

### Configure Environment Variable
Create a ```.env```file inside ```/src```:
```
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=hdb_resales
```
