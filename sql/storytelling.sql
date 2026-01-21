SELECT *
FROM resales_prices

---------------------------------------------------------------------------
-- Scenario: Late 30s couple, The Lims with a young child of 4 years old looking to upgrade from a 
-- 3 room flat in Jurong East to a 4 room flat in Clementi to be near a variety of good schools 

-- ==========================================================
-- Objective: Find cost of a 4 Room flat in Clementi estate 
-- Average Resale Price in Clementi estate for 4 ROOM flats
-- Shows average pricing for 4 rooms flats in Clementi in 2025
-- This query provides an estimated budget for the couple 
-- ==========================================================

SELECT town, 
       ROUND(AVG(resale_price), 0) AS avg_resale_price
FROM resales_prices
WHERE town = 'CLEMENTI' AND 
      flat_type = '4 ROOM' AND
	  resale_year = 2025
GROUP BY town

CREATE VIEW avg_price_4_room_clementi AS                     -- Create view for the Avg Price for 4 Room Clementi in 2025
SELECT town, 
       ROUND(AVG(resale_price), 0) AS avg_resale_price
FROM resales_prices
WHERE town = 'CLEMENTI' AND 
      flat_type = '4 ROOM' AND
	  resale_year = 2025
GROUP BY town; 

Select *
FROM avg_price_4_room_clementi

-- ==========================================================
-- Objective: Estimate a selling price for their 3 Room Flat in Jurong East  
-- Average Resale Price in Jurong East for 3 Room flats 
-- Shows the average price for 3 rooms flats in Jurong East transacted in 2025
-- This query provides an estimated value they could potentially sell their house for  
-- ==========================================================

SELECT town, ROUND(AVG(resale_price), 0) AS avg_resale_price
FROM resales_prices
WHERE town = 'JURONG EAST' AND 
      flat_type = '3 ROOM' AND
	  resale_year = 2025
GROUP BY town

CREATE VIEW avg_price_3_room_jurongeast AS                         -- Create view for the Avg Price for 3 Room Jurong East in 2025
SELECT town, ROUND(AVG(resale_price), 0) AS avg_resale_price
FROM resales_prices
WHERE town = 'JURONG EAST' AND 
      flat_type = '3 ROOM' AND
	  resale_year = 2025
GROUP BY town

SELECT * 
FROM avg_price_3_room_jurongeast


-- ==========================================================
-- Objective: Find a more affordable 4/5 Room hdb flat in their current estate with about 70 lease years left 
-- Average Resale Price in Jurong East for 4 Room flats with about 70 lease years 
-- Shows the average price for 4-5 rooms flats in Jurong East transacted in Sept 2025 onwards with 70 years left 
-- ==========================================================

SELECT town, flat_type, ROUND(AVG(resale_price), 0) AS avg_resale_price
FROM resales_prices
WHERE town = 'JURONG EAST' AND 
      flat_type IN ('4 ROOM', '5 ROOM') AND
	  resale_year = 2025 AND 
	  remaining_lease_years >= 69 AND
	  month >= DATE '2025-10-01'
GROUP BY town, flat_type


CREATE VIEW avg_price_4_and_5_room_jurongeast AS                              -- Create view for the Avg Price for 4/5 Room Jurong East in 2025 
SELECT town, flat_type, ROUND(AVG(resale_price), 0) AS avg_resale_price       -- with leasehold 70 years left for Q4 2025
FROM resales_prices
WHERE town = 'JURONG EAST' AND 
      flat_type IN ('4 ROOM', '5 ROOM') AND
	  resale_year = 2025 AND 
	  remaining_lease_years >= 69 AND
	  month >= DATE '2025-10-01'                     -- Q4 2025
GROUP BY town, flat_type

SELECT *
FROM avg_price_4_and_5_room_jurongeast


-- Comparison

SELECT town, flat_type, ROUND(AVG(resale_price), 0) AS avg_resale_price       
FROM resales_prices
WHERE town = 'JURONG EAST' AND 
      flat_type IN ('4 ROOM', '5 ROOM') AND
	  resale_year = 2025 AND 
	  remaining_lease_years >= 69 AND
	  month >= DATE '2025-01-01'                     -- Beginning of the year
GROUP BY town, flat_type

CREATE VIEW avg_price_jan_2025 AS                   -- Create view for price starting Jan 2025
SELECT town, flat_type, ROUND(AVG(resale_price), 0) AS avg_resale_price       
FROM resales_prices
WHERE town = 'JURONG EAST' AND 
      flat_type IN ('4 ROOM', '5 ROOM') AND
	  resale_year = 2025 AND 
	  remaining_lease_years >= 69 AND
	  month >= DATE '2025-01-01'                     
GROUP BY town, flat_type

SELECT *
FROM avg_price_jan_2025

--------------------------- End of story ---------------------------------
