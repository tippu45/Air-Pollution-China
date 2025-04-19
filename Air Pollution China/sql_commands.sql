-- show tables commnad
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';

-- select data command
SELECT * FROM "Air_Pollution_Data";

-- verfication step code
SELECT COUNT(*) FROM "Air_Pollution_Data";
