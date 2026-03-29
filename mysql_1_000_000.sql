USE db_1000000;




SELECT d.Nombre, l.Valor, l.Fecha
FROM Dispositivo d
INNER JOIN Lectura l ON d.ID = l.DispositivoID
WHERE d.ID = 2821;


UPDATE Lectura
SET Estado = 'Revisado'
WHERE Fecha = '2026-03-27';


CREATE INDEX idx_fecha ON Lectura(Fecha);


SELECT table_schema AS Base_de_Datos,
       ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS Tamaño_MB
FROM information_schema.TABLES
WHERE table_schema = 'db_10000'
GROUP BY table_schema;