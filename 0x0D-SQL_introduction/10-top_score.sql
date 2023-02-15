-- Lists all records of the table second_table of a database in MySQL server.
-- Results displayed as score then name, ordered by score (top first).
-- The database name will be passed as an argument of mysql command.
SELECT score, name FROM second_table ORDER BY score DESC;
