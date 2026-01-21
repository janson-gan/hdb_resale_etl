-- Data Integrity Queries to ensure data is not corrupted and have no null values. 

-- To check if there are no null values 
SELECT COUNT(*)
FROM resales_prices 
WHERE NOT (resales_prices IS NOT NULL)

-- To check that numericals fall in expected range
SELECT MIN(resale_price) as min_amount, MAX(resale_price) as max_amount 
FROM resales_prices 