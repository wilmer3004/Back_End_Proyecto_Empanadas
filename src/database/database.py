from decouple import config
import psycopg2

def get_db_conecction():
    try:
        # Use the config function to get the enviroment variables
        connection = psycopg2.connect(
            host=config('POSTGRES_HOST'),
            user=config('POSTGRES_USER'),
            password=config('POSTGRES_PASSWORD'),
            dbname=config('POSTGRES_DB'),
            port=int(config('POSTGRES_PORT'), default = 5432),

        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None