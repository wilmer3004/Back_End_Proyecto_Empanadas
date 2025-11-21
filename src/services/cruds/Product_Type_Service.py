from src.services.interfaces.Crud_Interface import Crud_Interface
from src.models.cruds.Product_Type_Model import Product_Type_Model
from src.database.database import get_db_conecction

class Product_Type_Service(Crud_Interface):
    
    # Implementing the abstract method from Crud:Interface
    
    # Consult all product types
    @classmethod
    def consult(cls):
        # Implement the logic to retrieve all product types from the database
        try:
            connection = get_db_conecction()
            product_Types = []
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM product_type')
                result_product_type = cursor.fetchall()
                for row in result_product_type:
                    product_type = Product_Type_Model(row[0],row[1],row[2],row[3])
                    product_Types.append(product_type.to_dict())
                connection.commit()
            return product_Types
        except Exception as e:
            print("An error ocurred: {e}")
        
        finally:
            connection.close()
            
        # Create a new product type
    @classmethod
    def create (cls, data):
        # Implement the logic to create a new product type in the database
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                sql = 'INSERT INTO product_type (name_product_type,detail_product_type) VALUES (%s, %s)'
                data_tuple = (data['name_product_type'], data['detail_product_type'])
                cursor.execute(sql,data_tuple)
                connection.commit()
                return {"message":"Product type created successfully"}
        
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error":"Failed to insert product type", "code":500}
        
        finally:
            connection.close()
    
    # Consult a product type by ID
    @classmethod 
    def consult_id(cls,id):
        # Implement the logic to retrieve a product type by ID from the database
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM product_type WHERE id_product_type = %s'
                cursor.execute(sql,(id,))
                row = cursor.fetchone()
                if row:
                    product_type = Product_Type_Model(row[0],row[1],row[2],row[3])
                    return product_type.to_dict()
                return {"error":"Product type not found", "code":404}
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error":"Failed to retrieve prodcut type", "code":500}
        finally:
            connection.close()
        
    # Update a product type by ID
    @classmethod
    def update (cls, id, data):
        # Implement the logic to update a product type in the database
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries 
            with connection.cursor() as cursor:
                sql = "UPDATE product_type SET name_product_type = %s, detail_product_type = %s WHERE id_product_type = %s"
                data_tuple = (data['name_product_type'], data['detail_product_type'], id)
                cursor.execute(sql, data_tuple)
                connection.commit()
                if cursor.rowcount == 0:
                    return {"error":"Product type not found", "code":404}
                return {"message":"Product type updated successfully"}
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error":"Failed to update priduct type", "code":500}
        finally:
            connection.close()
    
    # Change the state of a product type by id(activate/deactivate)
    @classmethod
    def change_state(cls, id):
        # Implement the logic to change the state of a product type in the database
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql_get_state = "SELECT state_product FROM product_type WHERE id_product_type = %s"
                cursor.execute(sql_get_state, (id,))
                row = cursor.fetchone()
                
                if not row:
                    return {"error":"Product_type not found", "code":404}
                
                current_state = row[0]
                new_state = not current_state
                
                sql = "UPDATE product_type SET state_product = %s WHERE id_product_type = %s"
                cursor.execute(sql, (new_state, id))
                connection.commit()
                return {"message":"Product type state changed successfully"}
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error":"Failed to change product type state","code":500}

        finally:
            connection.close()
                
    