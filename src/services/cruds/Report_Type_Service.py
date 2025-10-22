from src.services.interfaces.Crud_Interface import Crud_Interface
from src.models.cruds.Report_Type_Model import Report_Type_Model
from src.database.database import get_db_conecction

class Report_Type_Service(Crud_Interface):
    # Implementing the abstrac method from Crud_Interface
    # Consult all report types
    @classmethod
    def consult(cls):
        # Implement the logic to retrieve all report types from the database
        try:
            connection = get_db_conecction()
            report_types = []
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM report_type')
                result_report_type = cursor.fetchall()
                for row in result_report_type:
                    report_type = Report_Type_Model(row[0], row[1], row[2],row[3])
                    report_types.append(report_type.to_dict())
                connection.commit()
            return report_types
        # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error ocurred: {e}")
        # Ensure the connection is closed in the finally block
        finally:
            connection.close()
            
    # Create a new report type
    @classmethod 
    def create(cls, data):
        # Implement the logic to create a new report type in the database
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                sql = 'INSERT INTO report_type (name_report_type, detail_report_type) VALUES (%s,%s)'
                data_tuple = (data['name_report_type'], data['detail_report_type'])
                cursor.execute(sql, data_tuple)
                connection.commit()
                return {"message": "Report type created successfully"}
        # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error": "Failed to insert report type", "code": 500}
        # Ensure the connection is closed in the finally block
        finally:
            connection.close()
    
    # Consult a document type by ID
    @classmethod 
    def consult_id(cls, id):
        # Implement the logic to retrieve a report type by ID from the database
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM report_type WHERE id_report_type = %s'
                cursor.execute(sql, (id,))
                row = cursor.fetchone()
                if row:
                    report_type = Report_Type_Model(row[0], row[1], row[2], row[3])
                    return report_type.to_dict()
                else:
                    return None
        # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error ocurred: {e}")
        # Ensure the connection is closed in the finally block
        finally:
            connection.close()
    
    # Update a report type by ID
    @classmethod
    def update(cls, id, data):
        # Implement the logic to update a report type by ID in the database
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                sql = 'UPDATE report_type SET name_report_type = %s, detail_report_type = %s, state_report_type = %s WHERE id_report_type = %s'
                data_tuple = (data['name_report_type'], data['detail_report_type'], data['state_report_type'], id)
                cursor.execute(sql, data_tuple)
                connection.commit()
                return {"message": "Report type updated successfully"}
        # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error": "Failed to update report type", "code": 500}
        # Ensure the connection is closed in the finally block
        finally:
            connection.close()
    
    # Change the state of a report type by ID
    @classmethod
    def change_state(cls, id):
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                # First, get the current state
                sql_select = 'SELECT state_report_type FROM report_type WHERE id_report_type = %s'
                cursor.execute(sql_select, (id,))
                row = cursor.fetchone()
                if row:
                    current_state = row[0]
                    # Toggle the state
                    new_state = not current_state
                    sql_update = 'UPDATE report_type SET state_report_type = %s WHERE id_report_type = %s'
                    cursor.execute(sql_update, (new_state, id))
                    connection.commit()
                    return {"message": "Report type state changed successfully"}
                else:
                    return {"error": "Report type not found", "code": 404}
        # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error": "Failed to change report type state", "code": 500} 
        # Ensure the connection is closed in the finally block
        finally:
            connection.close()