import csv
import random
import sys
import os

def generar(num_lecturas):
    os.makedirs('data', exist_ok=True)
    
    print("Generando 1000 Dispositivos...")
    with open('data/dispositivo.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Nombre', 'Ubicacion'])
        for i in range(1, 1001):
            writer.writerow([i, f'Sensor_{i}', f'Zona_{random.randint(1, 50)}'])

    print(f"Generando {num_lecturas} Lecturas...")
    with open('data/lectura.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'DispositivoID', 'Fecha', 'Valor', 'Estado'])
        for i in range(1, num_lecturas + 1):
            # Asigna cada lectura a un DispositivoID aleatorio (Relación 1 a N)
            writer.writerow([i, random.randint(1, 1000), '2026-03-27', round(random.uniform(20.0, 100.0), 2), 'Activo'])
    print("Archivos generados en la carpeta /data.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python generar_datos.py <cantidad_lecturas>")
        sys.exit(1)
    generar(int(sys.argv[1]))