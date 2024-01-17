-- lists number of records with same score
ELECT `score`, COUNT(*) AS `number` FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
