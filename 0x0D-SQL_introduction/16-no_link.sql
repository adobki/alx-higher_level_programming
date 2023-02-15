-- Lists all records with a `name` in `second_table` in MySQL server.
-- Results displayed as score then name, ordered by score (top first).
-- The database name will be passed as an argument of mysql command.
SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
