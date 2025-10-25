from src.services.interfaces.Crud_Interface import Crud_Interface
from src.models.cruds.User_Emp_Model import User_Emp_Model
from src.database.database import get_db_conecction

# Implementing the abstrac method from Crud_Interface
class User_Emp_Service(Crud_Interface):
    
    # Consult all user emps
    @classmethod
    def consult(cls):
        #Implement the logic to retreive all user from the database
        try:
            connection = get_db_conecction()
            user_emps = [] 
            # Using a cursor to execute SQL queries 
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM user_emp')
                result_user_emp = cursor.fetchall()
                for row in result_user_emp:
                    user_emp = User_Emp_Model(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    user_emps.append(user_emp.to_dict())
                connection.commit()
            return user_emps
        
        except Exception as e:
            print(f"An error ocurred: {e}")
        
        finally:
            connection.close()
    
    # Create a new user emp
    @classmethod
    def create(cls, data):
        #Implement the logic to create a new user emp in the database 
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries 
            with connection.cursor() as cursor:
                sql = 'INSERT INTO user_emp (username, password_user,  id_rol_fk, id_person_fk) VALUES (%s, %s, %s, %s)'
                data_tuple = (data['username_user'], data['password_user'], data['id_rol_fk'], data['id_person_fk'])
                cursor.execute(sql, data_tuple)
                connection.commit()
                return {"message": "User emp created successfully"}
        
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error":"Failed to insert user emp", "code":500}
        
        finally:
            connection.close()
    
    # Consult a user emp by ID
    @classmethod
    def consult_id(cls, id):
        #Implement the logic to retreive a user emp by ID from the database
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries 
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM user_emp WHERE id_user = %s'
                cursor.execute(sql, (id,))
                row = cursor.fetchone()
                if row:
                    user_emp = User_Emp_Model(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    return user_emp.to_dict()
                return None
        
        except Exception as e:
            print(f"An error ocurred: {e}")
        
        finally:
            connection.close()

    # Update a user emp by ID
    @classmethod
    def update(cls, id, data):
        #Implement the logic to update a user emp by ID in the database 
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries 
            with connection.cursor() as cursor:
                sql = '''UPDATE user_emp 
                         SET username = %s, password_user = %s, id_rol_fk = %s, id_person_fk = %s
                         WHERE id_user = %s'''
                data_tuple = (data['username_user'], data['password_user'], data['id_rol_fk'], data['id_person_fk'], id)
                cursor.execute(sql, data_tuple)
                connection.commit()
                return {"message": "User emp updated successfully"}
        
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error":"Failed to update user emp", "code":500}
        
        finally:
            connection.close()
        
    # Change state of a user emp by ID
    @classmethod
    def change_state(cls, id):
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                # First, get the current state of the user emp
                sql_select = 'SELECT state_user FROM user_emp WHERE id_user = %s'
                cursor.execute(sql_select, (id,))
                row = cursor.fetchone()
                if not row:
                    return {"error": "User emp not found", "code": 404}
                current_state = row[0]
                # Toggle the state
                new_state = not current_state
                sql_update = 'UPDATE user_emp SET state_user = %s WHERE id_user = %s'
                cursor.execute(sql_update, (new_state, id))
                connection.commit()
                return {"message": "User emp state changed successfully"}
        
        # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error":"Failed to change user emp state", "code":500}
        finally:
            connection.close()
            