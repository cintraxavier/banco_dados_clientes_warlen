import sqlite3

conn = sqlite3.connect('cars.db')
cursor = conn.cursor()

# lendo os dados
cursor.execute("""
SELECT * FROM clientes;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()