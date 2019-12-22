operator

USE sql_store;
SELECT *
FROM mytable
WHERE modified_at > "2019-09-09T00:00:00" AND
optionsenable_all_notification = 'true'

-- compare with this:
optionsenable_all_notification = 1


if we want to know the number of records


SELECT count(*)