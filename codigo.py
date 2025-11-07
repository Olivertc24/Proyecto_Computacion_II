import sqlite3
import pandas as pd

# 1. Definir el SQL para el esquema
sql_crear_asegurados = """
CREATE TABLE IF NOT EXISTS Asegurados (
    id_asegurado TEXT PRIMARY KEY,
    edad INTEGER NOT NULL,
    sexo TEXT,
    region TEXT
);"""

sql_crear_polizas = """
CREATE TABLE IF NOT EXISTS Polizas (
    id_poliza TEXT PRIMARY KEY,
    id_asegurado TEXT,
    tipo_seguro TEXT NOT NULL,
    prima REAL,
    suma_asegurada REAL,
    fecha_inicio DATE,
    FOREIGN KEY (id_asegurado) REFERENCES Asegurados (id_asegurado)
);"""

# ¡Añadí esta que faltaba en tu captura!
sql_crear_siniestros = """
CREATE TABLE IF NOT EXISTS Siniestros (
    id_siniestro TEXT PRIMARY KEY,
    id_poliza TEXT,
    fecha_evento DATE NOT NULL,
    monto_reclamado REAL,
    monto_pagado REAL,
    estado TEXT,
    FOREIGN KEY (id_poliza) REFERENCES Polizas (id_poliza)
);"""


# --- ESTA ES LA PARTE CLAVE QUE DEBE EJECUTARSE ---

try:
    # 2. Conectar y crear la base de datos
    conn = sqlite3.connect('actuaria.db')
    cursor = conn.cursor()

    # 3. Ejecutar el SQL
    cursor.execute(sql_crear_asegurados)
    cursor.execute(sql_crear_polizas)
    cursor.execute(sql_crear_siniestros)

    # 4. Confirmar cambios 
    conn.commit()
    print("¡Base de datos y tablas creadas exitosamente!")

except sqlite3.Error as e:
    print(f"Ocurrió un error: {e}")

finally:
    # 5. Cerrar la conexión
    if conn:
        conn.close()

