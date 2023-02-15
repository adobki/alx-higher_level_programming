-- Lists records with `score` >= 10 from `second_table` of a database in MySQL
-- server. Displayed as `score` then `name`, ordered by `score` (top first).
-- The database name will be passed as an argument of mysql command.
SELECT score, name FROM second_table WHERE score >=10 ORDER BY score DESC;
