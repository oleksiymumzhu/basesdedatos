import csv
import random
import os
#test

CANTIDAD_LECTURAS = 100000000
CANTIDAD_DISPOSITIVOS = 100000000


carpeta = f'data/{CANTIDAD_LECTURAS}'
os.makedirs(carpeta, exist_ok=True)

print(f"Generando datos en {carpeta}...")
with open(f'{carpeta}/dispositivo.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Nombre', 'Ubicacion'])
    for i in range(1, CANTIDAD_DISPOSITIVOS + 1):
        writer.writerow([i, f'Sensor_{i}', f'Zona_{random.randint(1, 50)}'])

with open(f'{carpeta}/lectura.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'DispositivoID', 'Fecha', 'Valor', 'Estado'])
    for i in range(1, CANTIDAD_LECTURAS + 1):
        writer.writerow([i, random.randint(1, CANTIDAD_DISPOSITIVOS), '2026-03-27', round(random.uniform(20.0, 100.0), 2), 'Activo'])

print("Archivos generados exitosamente.")