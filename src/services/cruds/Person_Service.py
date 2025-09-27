from src.services.interfaces.Crud_Interface import Crud_Interface
from src.models.cruds.Person_Model import Person_Model
from src.database.database import get_db_conecction

class Person_Service(Crud_Interface):
    
    # Implementing the abstract methods from Crud_Interface
    # Consult all persons
    @classmethod
    def consult(cls):
        # Implement the logic to retrieve all persons from the database
        try:
            connection = get_db_conecction()
            people = []
            
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM person")
                result_person = cursor.fetchall()
                for row in result_person:
                    person = Person_Model(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                    people.append(person.to_dict())
                connection.commit()
            return people
        
        # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error occurred: {e}")
        
        # Ensure the connection is closed in the finally block
        finally:
            connection.close()
    
    # Create a new person
    @classmethod
    def create(cls, data):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql = """INSERT INTO person (id_document_type_fk, doc_person, first_name_person, second_name_person, first_last_name_person, second_last_name_person, email_person, phone_person, address_person) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                data_tuple = (data['id_document_type_fk'], data['doc_person'], data['first_name_person'], data['second_name_person'], data['first_last_name_person'], data['second_last_name_person'], data['email_person'], data['phone_person'], data['address_person'])
                cursor.execute(sql, data_tuple)
                connection.commit()
                return {"message": "Person created successfully"}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to insert person", "code": 500}
        finally:
            connection.close()
    
    # Consult a person by ID
    @classmethod
    def consult_id(cls, id):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql = "SELECT * FROM person WHERE id_person = %s"
                cursor.execute(sql, (id,))
                row = cursor.fetchone()
                if row:
                    person = Person_Model(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                    return person.to_dict()
                else:
                    return {"error": "Person not found", "code": 404}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to retrieve person", "code": 500}
        finally:
            connection.close()
            
    @classmethod
    def update(cls, id, data):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql = """UPDATE person SET id_document_type_fk=%s, doc_person=%s, first_name_person=%s, second_name_person=%s, first_last_name_person=%s, second_last_name_person=%s, email_person=%s, phone_person=%s, address_person=%s WHERE id_person=%s"""
                data_tuple = (data['id_document_type_fk'], data['doc_person'], data['first_name_person'], data['second_name_person'], data['first_last_name_person'], data['second_last_name_person'], data['email_person'], data['phone_person'], data['address_person'], id)
                cursor.execute(sql, data_tuple)
                connection.commit()
                if cursor.rowcount == 0:
                    return {"error": "Person not found", "code": 404}
                return {"message": "Person updated successfully"}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to update person", "code": 500}
        finally:
            connection.close()

    @classmethod
    def change_state(cls, id):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                # First, check the current state of the person
                sql_check = "SELECT state_person FROM person WHERE id_person = %s"
                cursor.execute(sql_check, (id,))
                row = cursor.fetchone()
                if not row:
                    return {"error": "Person not found", "code": 404}
                
                current_state = row[0]
                new_state = not current_state  # Toggle the state
                
                # Update the state
                sql_update = "UPDATE person SET state_person = %s WHERE id_person = %s"
                cursor.execute(sql_update, (new_state, id))
                connection.commit()
                
                return {"message": "Person state changed successfully", "new_state": new_state}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to change person state", "code": 500}
        finally:
            connection.close()