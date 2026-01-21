# table schema
from sqlalchemy import Table, Column, Integer, MetaData, Date, Numeric, VARCHAR

metadata = MetaData()

resales_prices = Table(
    "resales_prices",
    metadata,
    Column("month", Date, nullable=False),
    Column("town", VARCHAR(50), nullable=False),
    Column("flat_type", VARCHAR(20), nullable=False),
    Column("block", VARCHAR(10), nullable=False),
    Column("street_name", VARCHAR(100), nullable=False),
    Column("storey_range", VARCHAR(20), nullable=False),
    Column("floor_area_sqm", Numeric(6,2), nullable=False),
    Column("flat_model", VARCHAR(50), nullable=False),
    Column("lease_commence_date", Integer, nullable=False),
    Column("remaining_lease", VARCHAR(30), nullable=True),
    Column("resale_price", Numeric(12,2), nullable=False),
    Column("resale_year", Integer, nullable=False),
    Column("resale_month", Integer, nullable=False),
    Column("resale_quarter", Integer, nullable=True),
    Column("remaining_lease_years", Integer, nullable=True),
    Column("flat_age_years", Integer, nullable=False),
    Column("price_per_sqm", Numeric(10,2), nullable=False),
    Column("flat_age_category", VARCHAR(30), nullable=True),
    Column("price_category", VARCHAR(30), nullable=True),
    Column("region", VARCHAR(30), nullable=True)
    )