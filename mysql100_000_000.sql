USE db_100000000;

SELECT DispositivoID, COUNT(*) as Total
FROM Lectura
GROUP BY DispositivoID
ORDER BY Total DESC
LIMIT 1;