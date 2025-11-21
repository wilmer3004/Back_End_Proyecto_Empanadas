from src.database.database import get_db_conecction
from decouple import config
import jwt
import pytz
import datetime


class Security:
    
    tz = pytz.timezone(config("TIMEZONE"))
    secret_key = config("SECRET_KEY_JWT")
    
    # Generate JWT token
    @classmethod
    def generate_token(cls, autenticacion_usuario: dict):
        connection = None  # Prevents UnboundLocalError
        
        # 1. Generate JWT
        try:
            payload = {
                'iat': datetime.datetime.now(tz=cls.tz),
                'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(hours=1),
                'user_name': autenticacion_usuario['user_name'],
                'id_person_fk': autenticacion_usuario["id_person_fk"],
                'id_rol_fk': autenticacion_usuario["id_rol_fk"]
            }
            token = jwt.encode(payload, cls.secret_key, algorithm="HS256")

        except Exception as e:
            print(f"An error occurred while generating token: {e}")
            return None

        # 2. Save the token in DB
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql = """
                    UPDATE user_emp 
                    SET token_user = %s 
                    WHERE id_user = %s
                """
                cursor.execute(sql, (token, autenticacion_usuario["id_user"]))
                connection.commit()

            return token

        except Exception as e:
            print(f"An error occurred while saving token to database: {e}")
            return None

        finally:
            if connection:
                connection.close()



    
    # Verify JWT token
 # Validate JWT token and check whether it exists in the database
    @classmethod
    def verify_token(cls, headers):

        # 1. Validate that Authorization header is present
        if "Authorization" not in headers:
            print("Authorization header not found")
            return False
        
        # Extract the token
        auth_header = headers["Authorization"]
        try:
            token = auth_header.split(" ")[1]
        except:
            print("Invalid Authorization header format")
            return False
        
        # 2. Validate JWT signature and expiration
        try:
            payload = jwt.decode(token, cls.secret_key, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            print("Token has expired")
            return False
        except jwt.InvalidTokenError:
            print("Invalid token")
            return False
        
        # 3. Validate token existence in database
        connection = None
        try:
            connection = get_db_conecction()

            query = """
                SELECT id_user
                FROM user_emp
                WHERE token_user = %s
            """

            # Using context manager for the cursor
            with connection.cursor() as cursor:
                cursor.execute(query, (token,))
                result = cursor.fetchone()

            # Token exists
            if result:
                return True
            else:
                print("Token not found in database")
                return False

        except Exception as e:
            print(f"Database error while verifying token: {e}")
            return False

        finally:
            # Ensure the database connection is always closed
            if connection:
                connection.close()
    
    
    
    
    
    
    


