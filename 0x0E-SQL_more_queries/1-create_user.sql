-- Creates a MySQL server user user_0d_1 with all priviledges on the server.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
