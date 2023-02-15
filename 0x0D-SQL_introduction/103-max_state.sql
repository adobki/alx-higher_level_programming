-- Displays max temperature of each `state`, sorted by `state` in descending
-- order from `temperatures` in a database in MySQL server.
-- The database name will be passed as an argument of mysql command.
SELECT DISTINCT state, MAX(value) as 'max_temp' FROM temperatures GROUP BY state ORDER BY state;
