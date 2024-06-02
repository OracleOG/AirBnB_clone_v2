--  Creates a MySQL server with:
--    A database hbnb_dev_db
--    A new user hbnb_dev (in localhost)
--    password of hbnb_dev should match hbnb_dev_pwd
--    hbnb_dev(user) has all privileges on the database hbnb_dev_db(only)
--    hbnb_dev should have SELECT privilege on the database performance_schema(only)

--  create a new database hbnb_dev_db, if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

--  Create a new user hbnb_dev (in localhost)
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- hbnb_dev(user) has all privileges on the database hbnb_dev_db(only)
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- hbnb_dev has SELECT privilege on the database performance_schema(only)
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges for changes
FLUSH PRIVILEGES;
