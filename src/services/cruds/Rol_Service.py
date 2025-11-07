from src.services.interfaces.Crud_Interface import Crud_Interface
from src.models.cruds.Rol_Model import Rol_Model
from src.database.database import get_db_conecction

class Rol_Service(Crud_Interface):
    
    #Implementing the abstract methods from Crud_interface
    #Consult all roles
    @classmethod
    def consult(cls):
        #Implement the logic to retrieve all persons from the database
        try:
            connection = get_db_conecction()
            people=[]
            
            #Usign a cursor to execute SQL queries
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM rol")
                result_rol = cursor.fetchall()
                for row in result_rol:
                    rol = Rol_Model (row[0], row[1], row[2])
                    people.append(rol.to_dict())
                connection.commit()
            return people
        # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error ocurred:{e}")
        #Ensure the connection is closed in the finally block
        finally:
            connection.close()
    
    def create(cls, data):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql = """INSERT INTO rol (name_rol) VALUES (%s)"""
                data_tuple = (data["name_rol"])
                cursor.execute(sql, data_tuple)
                connection.commit()
                return{"message": "Rol created successfully"}
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"message": "Failed to insert rol","code": 500}
        finally:
            connection.close()
            
# Consult a rol by ID
@classmethod
def consult_id(cls,id):
    try:
        connection = get_db_conecction()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM rol WHERE id_rol = %s"
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
            if row:
                rol = Rol_Model(row[0], row[1], row [2])
                return rol.to_dict()
            else:
                return{"error": "Rol not found", "code": 404}
    except  Exception as e:
        print(f"An error ocurred: {e}")
        return {"error": "Failed to retrieve rol", "code": 500}
    finally:
        connection.close()
@classmethod
def update(cls,id,data):
    try:
        connection = get_db_conecction()
        with connection.cursor() as cursor:
            sql ="""UPDATE Rol name_rol WHERE id_rol=%s"""
            data_tuple =(data["name_rol"],id)
            cursor.excurte(sql,data_tuple)
            connection.commit()
            if cursor.rowcount == 0:
                return {"error": "Rol not found", "code": 404}
            return {"message" "Rol updated successfuly"}
    except Exception as e:
        print(f"An error ocurred: {e}")
        return {"error": "Failed to update person", "code": 500}
    finally:
        connection.close()
    @classmethod
    def  change_state(cls,id):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                #Firs, check the current state of the role
                sql_check = "SELECT state_rol FROM person WHERE id_rol = %s"
                cursor.execute(sql_check,(id,))
                row = cursor. fetchone()
                if not row:
                    return{"error": "Rol not found", "code": 404}
                
                current_state = row[0]
                new_state = not current_state
                
            # Update the state
            sql_update = "UPDATE rol SET state_rol = %s WHERE id_rol =%s"
            cursor.execute(sql_update, (new_state,id))
            connection.commit()
            
            return {"message": "Rol state changed successfully", "new_state": new_state}
        except Exception as e:
            print(f"An error ocurred: (e)")
            return {"error": "Failed to change state_rol", "code": 500}
        finally:
            connection.close()
    
            
                