from src.services.interfaces.Crud_Interface import Crud_Interface
from src.models.cruds.Document_Type_Model import Document_Type_Model
from src.database.database import get_db_conecction

class Document_Type_Service(Crud_Interface):

    # Implementing the abstrac method from Crud_Interface
    # Consult all document types 
    
    @classmethod
    def consult(cls):
        # implement the logic to retreive all document types from the database
        try:
            connection = get_db_conecction()
            document_types=[]

            # Using a cursor to execute SQL queries 
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM document_type')
                result_document_type = cursor.fetchall()
                for row in result_document_type:
                    document_type = Document_Type_Model(row[0], row[1], row[2], row[3])
                    document_types.append(document_type.to_dict())
                connection.commit()
            return document_types
        
        # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error ocurred: {e}")
        
        # Ensure the connection is closed in the finally block

        finally:
            connection.close()

    # Create a new document type 
    @classmethod
    def create(cls, data):
        
        # implement the logic to create a new document type in the database 
        try:
            connection = get_db_conecction()
        # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                
                sql = 'INSERT INTO document_type (name_document_type, acronym_document_type) VALUES (%s, %s)'
                data_tuple = (data['name_document_type'], data['acronym_document_type'])
                cursor.execute(sql, data_tuple)
                connection.commit()
                return {"message": "Document type created successfully"}
            # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error":"Failed to insert document type", "code":500}
        # Ensure the connection is closed in the finally block
        finally:
            connection.close()
    
    # Consult a document type by ID
    @classmethod
    def consult_id(cls, id):
        # Implement the logic to retrieve a document type by ID from the database
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM document_type WHERE id_document_type = %s'
                cursor.execute(sql,(id,))
                row = cursor.fetchone()
                # If a row is found, create a Document_Type_Model instance and return its dictionary representation
                if row:
                    document_type = Document_Type_Model(row[0], row[1], row[2], row[3])
                    return document_type.to_dict()
                return {"error":"Document type not found", "code":404}
        # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error ocurerred: {e}")
            return {"error":"Failed to retrieve document type", "code":500}
        # Ensure the connection is closed in the finally block
        finally:
            connection.close()
    
    # Update a document type details
    @classmethod
    def update(cls, id, data):
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                sql = 'UPDATE document_type SET name_document_type = %s, acronym_document_type = %s WHERE id_document_type = %s'
                data_tuple = (data['name_document_type'], data['acronym_document_type'], id)
                cursor.execute(sql, data_tuple)
                connection.commit()
                if cursor.rowcount == 0:
                    return {"error": "Document type not found", "code": 404}
                return {"message": "Document type updated successfully"}
            
        except Exception as e:
            print(f'An error ocurred: {e}')
            return {"error":"Failed to update document type", "code":500}
        finally:
            connection.close()
    
    # Change the state of a document type (activate/deactivate)
    @classmethod
    def change_state(cls, id):
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                sql_check = "SELECT state_document_type FROM document_type WHERE id_document_type = %s"
                cursor.execute(sql_check, (id,))
                row = cursor.fetchone()

                if not row:
                    return {"error": "Document type not found", "code": 404}
                
                current_state = row[0]  # Assuming state_document_type is the fourth column
                new_state = not current_state  # Toggle the state


                sql = "UPDATE document_type SET state_document_type = %s WHERE id_document_type = %s"
                cursor.execute(sql, (new_state, id))
                connection.commit()

                return {"message": "Document type state changed successfully", "new_state": new_state}
        # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error":"Failed to change document type state", "code":500}
        # Ensure the connection is closed in the finally block
        finally:
            connection.close()
    
    
                



    
