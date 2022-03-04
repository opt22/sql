USE db1; create table users(
user_id int PRIMARY KEY UNIQUE AUTO_INCREMENT,
user_name VARCHAR(100) NULL,
user_email VARCHAR(80) NOT NULL UNIQUE);
-- - - - - - - - - - 
--[.DATATYPES.]:
----
--CHAR(size) 	    A FIXED length string (can contain letters, numbers, and special characters).
--VARCHAR(size) 	    A VARIABLE length string (can contain letters, numbers, and special characters).
--BINARY(size) 	    Equal to CHAR(), but stores binary byte strings. The size parameter specifies the
--VARBINARY(size) 	Equal to VARCHAR(), but stores binary byte strings. The size parameter specifies
--TINYBLOB 	        For BLOBs (Binary Large Objects). Max length: 255 bytes
--TINYTEXT 	        Holds a string with a maximum length of 255 characters
--TEXT(size) 	    Holds a string with a maximum length of 65,535 bytes
--BLOB(size) 	    For BLOBs (Binary Large Objects). Holds up to 65,535 bytes of data
--MEDIUMTEXT 	    Holds a string with a maximum length of 16,777,215 characters
--MEDIUMBLOB 	    For BLOBs (Binary Large Objects). Holds up to 16,777,215 bytes of data
--LONGTEXT 	        Holds a string with a maximum length of 4,294,967,295 characters
--LONGBLOB 	        For BLOBs (Binary Large Objects). Holds up to 4,294,967,295 bytes of data
--ENUM(val1, val2, val3, ...) 	A string object that can have only one value, chosen from a list of
--SET(val1, val2, val3, ...) 	A string object that can have 0 or more values, chosen from a list of possible
-- - - - - - - - - - 
--[:Column Definitions:]
---
--PK                 PRIMARY KEY
--NN                 NULL / NOT NULL
--UQ                 UNIQUE
--BIN                ?
--UN                 ?
--ZF                 ZEROFILL                 #non standard, zero fills the value address
--AI                 AUTO_INCREMENT
--G                  ?
--Default/Expression DEFAULT (something)
--                   COMMENT "some comment"
--                   COMPRESSED
