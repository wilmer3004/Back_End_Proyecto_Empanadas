from src.services.interfaces.Crud_Interface import Crud_Interface
from src.models.cruds.Sale_Model import Sale_Model
from src.database.database import get_db_conecction

class Sale_Service(Crud_Interface):
    
    # Implementing the abstract method from Crud_Interface
    
    # Consult all sales
    @classmethod
    def consult(cls):
        # Implement the logic to retrieve all sales from the database
        try:
            connection = get_db_conecction()
            sales = []
            
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM sale')
                result_sales = cursor.fetchall()
                for row in result_sales:
                    sale = Sale_Model(row[0], row[1], row[2], row[3], row[4], row[5])
                    sales.append(sale.to_dict())
                connection.commit()
            return sales
        
        # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error ocurred: {e}")
        
        # Ensure the connection is closed in the finally block
        finally:
            connection.close()
    
    # Create a new sale
    @classmethod
    def create(cls, data):
        # Implement the logic to create a new sale in the database
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                sql = '''INSERT INTO sale (id_order_fk, date_sale, total_sale, type_sale) 
                         VALUES (%s, %s, %s, %s)'''
                data_tuple = (data['id_order_fk'], data['date_sale'], data['total_sale'], data['type_sale'])
                cursor.execute(sql, data_tuple)
                connection.commit()
                return {"message": "Sale created successfully"}
        # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error": "Failed to insert sale", "code": 500}
        # Ensure the connection is closed in the finally block
        finally:
            connection.close()
    
    # Consult a sale by ID
    @classmethod
    # Implement the logic to retrieve a sale by ID from the database
    def consult_id(cls, id):
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM sale WHERE id_sale = %s'
                cursor.execute(sql, (id,))
                row = cursor.fetchone()
                if row:
                    sale = Sale_Model(row[0], row[1], row[2], row[3], row[4], row[5])
                    return sale.to_dict()
                return None
        # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error ocurred: {e}")
        # Ensure the connection is closed in the finally block
        finally:
            connection.close()
            
    # Update a sale by ID
    @classmethod
    def update(cls, id, data):
        # Implement the logic to update a sale in the database
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                sql = '''UPDATE sale 
                         SET id_order_fk = %s, date_sale = %s, total_sale = %s, type_sale = %s
                         WHERE id_sale = %s'''
                data_tuple = (data['id_order_fk'], data['date_sale'], data['total_sale'], data['type_sale'], id)
                cursor.execute(sql, data_tuple)
                connection.commit()
                return {"message": "Sale updated successfully"}
        # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error": "Failed to update sale", "code": 500}
        # Ensure the connection is closed in the finally block
        finally:
            connection.close()
    
    # Change the state of a sale
    @classmethod
    def change_state(cls, id):
        # Implement the logic to change the state of a sale in the database
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                sql_check = 'SELECT state_sale FROM sale WHERE id_sale = %s'
                cursor.execute(sql_check, (id,))
                row = cursor.fetchone()
                
                if not row:
                    return {"error": "Sale not found", "code": 404}
                current_state = row[0]
                new_state = not current_state
                sql_update = 'UPDATE sale SET state_sale = %s WHERE id_sale = %s'
                cursor.execute(sql_update, (new_state, id))
                connection.commit()
                return {"message": "Sale state changed successfully"}
        # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error": "Failed to change sale state", "code": 500}
        # Ensure the connection is closed in the finally block
        finally:
            connection.close()
    