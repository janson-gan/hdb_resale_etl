-- ==========================================================
-- Average Resale Price by Flat Type
-- Shows how pricing differs across flat types (2R, 3R, 4R, etc)
-- Useful for identifying which flat types command higher prices
-- ==========================================================

SELECT
    flat_type,                               -- category of flat (e.g., 3 ROOM, 4 ROOM)
    ROUND(AVG(resale_price), 0) AS avg_resale_price   -- average price for each flat type
FROM resales_prices                           -- main dataset
GROUP BY flat_type                             -- group all records by flat type
ORDER BY avg_resale_price DESC;                -- show most expensive flat types first

/* 
--------------------------------------------------------------
Query flow:
From table resales_prices, group all transactions by flat_type.
For each flat type, compute the average resale price and round it
to the nearest whole dollar for readability. After calculating 
these averages, sort the results from highest to lowest so the 
most expensive flat types appear at the top.
--------------------------------------------------------------
*/

/* 
--------------------------------------------------------------
Query goal and expected outcome:
Produce a clear comparison of average prices across all flat types.
1. Helps identify which flat types are more expensive on average.
2. Provides context for pricing tiers (e.g., 2 ROOM vs 4 ROOM vs EXECUTIVE).
3. Supports descriptive storytelling about affordability and market structure.
--------------------------------------------------------------
*/


 
-- ==========================================================
-- Number of Transactions by Year
-- Shows yearly resale activity to reveal volume trends over time
-- Useful for understanding market demand and data distribution
-- ==========================================================

SELECT
    resale_year,                  -- extract the year of the transaction
    COUNT(*) AS num_transactions  -- total number of transactions in that year
FROM resales_prices               -- main table
GROUP BY resale_year              -- group all rows by year
ORDER BY resale_year;             -- show results chronologically

/* 
--------------------------------------------------------------
Query flow:
From table resales_prices, take every transaction and group them 
by resale_year. For each year, count the number of rows to find 
the total number of resale transactions recorded. Finally, order 
the results by year so you can see how the volume changes over time.
--------------------------------------------------------------
*/

/* 
--------------------------------------------------------------
Query goal and expected outcome:
Produce a year-by-year summary of transaction volume.
1. Highlights busy and slow years in the resale market.
2. Helps validate whether the dataset has coverage across years.
3. Supports trend analysis and ties into broader market conditions.
--------------------------------------------------------------
*/


-- ==========================================================
-- Monthly Price Trend
-- Shows average resale price per month to highlight the
-- overall upward trend, especially after 2020
-- ==========================================================

SELECT
    -- Truncate each date to the first day of its month
    DATE_TRUNC('month', month) AS month_start,

    -- Average resale price for that month, rounded to whole dollars
    ROUND(AVG(resale_price), 0) AS avg_resale_price
FROM resales_prices   -- use the main table name here
GROUP BY 1            -- group by month_start
ORDER BY 1;           -- sort by month_start from earliest to latest

/* 
--------------------------------------------------------------
Query flow:
From table resales_prices, take every transaction and group them
by calendar month using DATE_TRUNC('month', month). This converts 
any day within the month to the first day of that month so all 
sales inside the same month fall into one group. For each month, 
compute the average resale price and round it to a whole number. 
Finally, order the results from the earliest month to the latest 
to form a clean month-by-month trend series.
--------------------------------------------------------------
*/

/* 
--------------------------------------------------------------
Query goal and expected outcome:
Produce a monthly trend of average resale prices across all towns 
and flat types. This helps show how prices move over time and 
supports the narrative that resale prices steadily increased, 
especially after 2020. The result is a time-series dataset that 
can be used for charts or storytelling about market trends.
--------------------------------------------------------------
*/