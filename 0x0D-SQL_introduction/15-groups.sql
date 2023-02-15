-- Lists number of records with the same score in the table `second_table` of a
-- database in MySQL server. Results displayed as the score, then number of
-- records for the score with the label number, sorted in descending order.
-- The database name will be passed as an argument of mysql command.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
