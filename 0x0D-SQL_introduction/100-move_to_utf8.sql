-- Converts the following to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in MySQL
-- server: database hbtn_0c_0, table `first_table`, and field/column `name`.
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
