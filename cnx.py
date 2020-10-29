import psycopg2

host = "localhost"
port = "5432"
user = "postgres"
password = "@M4radona"
db = "loginapp"

try:
    conectar = "host=%s port=%s user=%s password=%s dbname=%s" % (
        host, port, user, password, db)
    conn = psycopg2.connect(conectar)
    print("Conexion Exitosa!")
except Exception as e:
    print(f"ha ocurrido un error: {e}")
