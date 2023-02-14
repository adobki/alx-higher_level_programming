-- Lists all the tables of a database in your MySQL server.
-- The database name will be passed as an argument of mysql command.
SET @db = ?;
USE @db; SHOW tables;
--SHOW TABLES FROM @db;
