from src.services.interfaces.Crud_Interface import Crud_Interface
from src.models.cruds.Customer_Type_Model import Customer_Type_Model
from src.database.database import get_db_conecction

class Customer_type_service(Crud_Interface):
    # Implementing the abstrac method from Crud_Interface
    # Consult all customer types

    @classmethod
    def consult(cls):
        # Implement the logic to retreive all customer types from the database
        try:
            connection = get_db_conecction()
            customer_types = []

            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM customer_type')
                result_customer_type = cursor.fetchall()
                for row in result_customer_type:
                    customer_type =  Customer_Type_Model(row[0],row[1],row[2],row[3])
                    customer_types.append(customer_type.to_dict())
                connection.commit()
            return customer_types
        # Handle exceptions and ensure the connection is closed 
        except Exception as e:
            print(f"An error ocurred: {e}")

        # Ensure the connection is closed in the finally block 
        finally:
            connection.close()
    
    # Create a new customer type
    @classmethod
    def create(cls, data):

        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql = "INSERT INTO customer_type (name_customer_type,detail_customer_type) VALUES (%s,%s)"
                data_tuple = (data['name_customer_type'], data['detail_customer_type'])
                cursor.execute(sql,data_tuple)
                connection.commit()
                return {"message": "Customer type created successfully"}
            
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error":"Failed to insert customer type", "code":500}
        finally:
            connection.close()

    # Consult a customer type by ID
    @classmethod
    def consult_id(cls, id):
        try:
            connection = get_db_conecction()

            with connection.cursor() as cursor:
                sql = 'SELECT * FROM customer_type WHERE id_customer_type = %s'
                cursor.execute(sql, (id,))
                row = cursor.fetchone()

                if row:
                    customer_type = Customer_Type_Model(row[0], row[1], row[2], row[3])
                    return customer_type.to_dict()
                return {'error': 'Customer type not found','code':404 }
        except Exception as e:
            print(f'An error ocurred: {e}')
            return {'error':'Failed to retrieve customer type','code':500}
        finally:
            connection.close()

    #Update a customer type details
    @classmethod
    def update(cls,id,data):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql = "UPDATE customer_type SET name_customer_type = %s, detail_customer_type = %s WHERE id_customer_type = %s"
                data_tuple = (data['name_customer_type'], data['detail_customer_type'], id)
                cursor.execute(sql, data_tuple)
                connection.commit()
                if cursor.rowcount == 0:
                    return {'error': 'Customer type not found', 'code': 404}
                return {"message": "Customer type updated successfully"}
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error":"Failed to update customer type", "code":500}
        finally:
            connection.close()

    # Change the state of a customer type (activate/deativate)
    @classmethod
    def change_state(cls, id):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                # First, retrieve the current state of the customer type
                sql_select = "SELECT state_customer_type FROM customer_type WHERE id_customer_type = %s"
                cursor.execute(sql_select, (id,))
                row = cursor.fetchone()

                if row:
                    current_state = row[0]
                    # Toggle the state
                    new_state = not current_state
                    sql_update = "UPDATE customer_type SET state_customer_type = %s WHERE id_customer_type = %s"
                    cursor.execute(sql_update, (new_state, id))
                    connection.commit()
                    return {"message": "Customer type state changed successfully"}
                return {"error": "Customer type not found", "code": 404}
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error":"Failed to change customer type state", "code":500}
        finally:
            connection.close()
     
