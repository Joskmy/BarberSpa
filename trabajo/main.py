import psycopg2

# Parámetros de conexión
host = "localhost"
database = "Final"
user = "postgres"
password = "chzpmn1001"

# Establecer conexión con la base de datos
try:
    connection = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = connection.cursor()
    print("Conexión establecida exitosamente con la base de datos PostgreSQL.")
    
    # Crear tabla
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Hola (
        id SERIAL PRIMARY KEY,
        columna1 VARCHAR(255),
        columna2 VARCHAR(255)
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
    print("La tabla Hola se ha creado correctamente.")

except (Exception, psycopg2.Error) as error:
    print("Error al conectar o crear la tabla:", error)

finally:
    # Cerrar la conexión
    if connection:
        cursor.close()
        connection.close()
        print("Conexión cerrada exitosamente.")
