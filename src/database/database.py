from decouple import config
import psycopg2

def get_db_conecction():
    try:
        connection = psycopg2.connect(
            host=config('POSTGRES_HOST', default='localhost'),
            user=config('POSTGRES_USER', default='postgres'),
            password=config('POSTGRES_PASSWORD', default='admin'),
            dbname=config('POSTGRES_DB', default='empanadas_db'),
            port=config('POSTGRES_PORT', default=5432, cast=int)
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
