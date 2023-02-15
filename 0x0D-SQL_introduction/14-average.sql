-- Computes the score average of all records in the table `second_table` of a
-- database in MySQL server. The `result` column name would be 'average'.
-- The database name will be passed as an argument of mysql command.
SELECT AVG(score) AS average FROM second_table;
