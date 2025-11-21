from src.security.model.Auth_Model import Auth_Model
from src.database.database import get_db_conecction
from src.security.service.interface.Auth_interface import Auth_Interface

class Auth_Service(Auth_Interface):
    
    @classmethod
    def login_user(cls, user_name, password_user):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql = """
                    SELECT id_user, id_rol_fk, id_person_fk, username, password_user, token_user, state_user
                    FROM user_emp
                    WHERE username = %s AND password_user = %s
                """
                cursor.execute(sql, (user_name, password_user))
                row = cursor.fetchone()
                if row:
                    auth_model = Auth_Model(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    return auth_model.to_dict()
                else:
                    return {"error": "Invalid username or password", "code": 401}
        except Exception as e:
            print(f"An error occurred during login: {e}")
            return {"error": "Failed to login", "code": 500}
        finally:
            connection.close()

