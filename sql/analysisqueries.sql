7.3 Analysis Queries 

-- Objective: Find average sale prices for most recent MOP flats 

-- What is the average resale price for flats recently MOP?                    
SELECT town, flat_type, ROUND(AVG(resale_price), 2) AS average_resale_price
FROM resales_prices
WHERE lease_commence_date = 2021 AND
      flat_type IN ('3 ROOM', '4 ROOM', '5 ROOM') AND
	  flat_model != 'DBSS'
GROUP BY town, flat_type
ORDER BY average_resale_price DESC


CREATE VIEW mop_avg_price AS                                                   -- Create view for average prices for recently MOP flats
SELECT town, flat_type, ROUND(AVG(resale_price), 2) AS average_resale_price
FROM resales_prices
WHERE lease_commence_date = 2021 AND
      flat_type IN ('3 ROOM', '4 ROOM', '5 ROOM') AND
	  flat_model != 'DBSS'
GROUP BY town, flat_type
ORDER BY average_resale_price DESC

SELECT *
FROM mop_avg_price

-----

-- Objective: Find the percentage increase in prices of flats MOP in 2020 vs flats MOP in 2021
-- What is the percentage increase from MOP flat prices 1 year ago from most recent MOP flats 
SELECT town, flat_type, ROUND((MAX(resale_price) - MIN(resale_price)):: numeric / MIN(resale_price) * 100, 2) AS increase_in_price
FROM resales_prices
WHERE flat_type IN ('3 ROOM', '4 ROOM', '5 ROOM') AND
      flat_model != 'Terrace' AND flat_model != 'DBSS' AND
	  lease_commence_date >= 2020 
GROUP BY town, flat_type
ORDER BY increase_in_price DESC

CREATE VIEW price_increase_percentage_mop_since_2020 AS                 -- Create view for % price increase for most recent MOP flats to 1 year ago 
SELECT town, flat_type, ROUND((MAX(resale_price) - MIN(resale_price)):: numeric / MIN(resale_price) * 100, 2) AS increase_in_price
FROM resales_prices
WHERE flat_type IN ('3 ROOM', '4 ROOM', '5 ROOM') AND
      flat_model != 'Terrace' AND flat_model != 'DBSS' AND
	  lease_commence_date >= 2020 
GROUP BY town, flat_type
ORDER BY increase_in_price DESC

SELECT *
FROM price_increase_percentage_mop_since_2020