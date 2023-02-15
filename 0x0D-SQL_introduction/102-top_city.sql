-- Displays top 3 city temperatures in July and August sorted by temperature
-- (`value`) in descending order from `temperatures` in MySQL server.
-- The database name will be passed as an argument of mysql command.
SELECT DISTINCT city, AVG(value) AS 'avg_temp' FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
