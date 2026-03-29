USE db_100000000;

SELECT d.Nombre, l.Valor, l.Fecha
FROM Dispositivo d
INNER JOIN Lectura l ON d.ID = l.DispositivoID
WHERE d.ID = 16649998;


UPDATE Lectura
SET Estado = 'Revisado'
WHERE Fecha = '2026-03-27';


CREATE INDEX idx_fecha ON Lectura(Fecha);


DELETE FROM Lectura
WHERE Estado = 'Activo';

ANALYZE TABLE Dispositivo, Lectura;

SELECT table_schema AS Base_de_Datos,
       ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS Tamaño_MB
FROM information_schema.TABLES
WHERE table_schema = 'db_100000000'
GROUP BY table_schema;



#EXTRA
SELECT DispositivoID, COUNT(*) as TotalLecturas, AVG(Valor) as Promedio
FROM Lectura
GROUP BY DispositivoID;


SELECT d.Nombre, AVG(l.Valor) as Promedio
FROM Dispositivo d
INNER JOIN Lectura l ON d.ID = l.DispositivoID
GROUP BY d.ID, d.Nombre
ORDER BY Promedio DESC
LIMIT 5;