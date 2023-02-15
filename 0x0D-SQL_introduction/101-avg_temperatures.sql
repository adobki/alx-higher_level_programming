-- Displays average temperature by city, sorted by temperature (`value`)
-- in descending order from `temperatures` of a database in MySQL server.
-- The database name will be passed as an argument of mysql command.
SELECT DISTINCT city, AVG(value) AS 'avg_temp' FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
