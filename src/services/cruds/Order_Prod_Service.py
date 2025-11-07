from src.services.interfaces.Crud_Interface import Crud_Interface
from src.models.cruds.Order_Product_Model import Order_Product_Model
from src.models.cruds.Order_Prod_Model import Order_Prod_Model
from src.database.database import get_db_conecction

class Order_Prod_Service(Crud_Interface):
    
    # Implementing the abstrac method from Crud_Interface
    # Consult all order products
    
    @classmethod
    def consult(cls):
        
        try:
            connection = get_db_conecction()
            order_products = []
            
            # Using a cursor to execute SQL queries
            
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM order_p')
                result_order_product = cursor.fetchall()
                

                # Iterate through the results and create Order_Prod_Model and Order_Product_Model objects
                for row in result_order_product:
                    # For each order, get its associated products
                    order_product_products = []
                    
                    cursor.execute('SELECT * FROM order_product WHERE id_order_p_fk = %s', (row[0],)) 
                    
                    result_order_product_products = cursor.fetchall()
                    order_product = Order_Prod_Model(row[0], row[1], row[2], row[3], row[4])
                    # Create Order_Product_Model objects for each associated product
                    for prod_row in result_order_product_products:
                        order_product_product = Order_Product_Model(prod_row[0], prod_row[1], prod_row[2])
                        order_product_products.append(order_product_product.to_dict()) 
                        # Append the order with its products to the main list
                    order_products.append({"id":row[0],"Order_product":order_product.to_dict(), "Products":order_product_products})  
                connection.commit()
            return order_products
        
        except Exception as e:
            print(f"An error ocurred: {e}")

        finally:
            connection.close()
    # Create a new order product
    @classmethod
    def create(cls, data):
        
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                
                sql = 'INSERT INTO order_p (id_customer_fk, detail_order, date_order, state_order) VALUES (%s, %s, %s, %s)'
                data_tuple = (data['id_customer_fk'], data['detail_order'], data['date_order'], data['state_order'])
                cursor.execute(sql, data_tuple)
                products = data['products']  # List of products to be added to the order
                order_id = cursor.lastrowid  # Get the ID of the newly created order
                # Insert each product into the order_product table
                for product in products:
                    sql_product = 'INSERT INTO order_product (id_order_p_fk, id_product_fk, quantity_product) VALUES (%s, %s, %s)'
                    data_product_tuple = (order_id, product['id_product_fk'], product['quantity_product'])
                    cursor.execute(sql_product, data_product_tuple)
                connection.commit()
                return {"message": "Order product created successfully"}
        
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error":"Failed to insert order product", "code":500}
        
        finally:
            connection.close()
    
    # Consult an order product by ID
    @classmethod
    def consult_id(cls, id):
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM order_p WHERE id_order_p = %s'
                cursor.execute(sql, (id,))
                row = cursor.fetchone()
                
                if row:
                    # Get associated products for the order
                    cursor.execute('SELECT * FROM order_product WHERE id_order_p_fk = %s', (id,))
                    result_order_product_products = cursor.fetchall()
                    order_product = Order_Prod_Model(row[0], row[1], row[2], row[3], row[4])
                    order_product_products = []
                    for prod_row in result_order_product_products:
                        order_product_product = Order_Product_Model(prod_row[0], prod_row[1], prod_row[2])
                        order_product_products.append(order_product_product.to_dict())
                    
                    connection.commit()
                    return {"Order_product":order_product.to_dict(), "Products":order_product_products}
                else:
                    return {"message": "Order product not found"}
        
        except Exception as e:
            print(f"An error ocurred: {e}")
        
        finally:
            connection.close()
    
    # Update an existing order product
    @classmethod
    def update(cls, id, data):
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                sql = 'UPDATE order_p SET id_customer_fk = %s, detail_order = %s, date_order = %s, state_order = %s WHERE id_order_p = %s'
                data_tuple = (data['id_customer_fk'], data['detail_order'], data['date_order'], data['state_order'], id)
                cursor.execute(sql, data_tuple)
                connection.commit()
                return {"message": "Order product updated successfully"}
        
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error":"Failed to update order product", "code":500}
        
        finally:
            connection.close()
    
    # Update the product within an order
    @classmethod
    def update_product(cls, order_id, data):
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                sql = 'UPDATE order_product SET quantity_product = %s WHERE id_order_p_fk = %s AND id_product_fk = %s'
                data_tuple = (data['quantity_product'], order_id, data['id_product_fk'])
                cursor.execute(sql, data_tuple)
                connection.commit()
                return {"message": "Order product item updated successfully"}
        
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error":"Failed to update order product item", "code":500}
        
        finally:
            connection.close()
    # Change the state of an order product (activate/deactivate)
    @classmethod
    def change_state(cls, id):
        try:
            connection = get_db_conecction()
            # Using a cursor to execute SQL queries
            with connection.cursor() as cursor:
                sql_check = "SELECT state_order FROM order_p WHERE id_order_p = %s"
                cursor.execute(sql_check, (id,))
                row = cursor.fetchone()

                if not row:
                    return {"error": "Order product not found", "code": 404}
                
                current_state = row[0]  # Assuming state_order is the fifth column
                new_state = not current_state  # Toggle the state


                sql = "UPDATE order_p SET state_order = %s WHERE id_order_p = %s"
                cursor.execute(sql, (new_state, id))
                connection.commit()

                return {"message": "Order product state changed successfully", "new_state": new_state}
        # Handle exceptions and ensure the connection is closed
        except Exception as e:
            print(f"An error ocurred: {e}")
            return {"error":"Failed to change order product state", "code":500}
        # Ensure the connection is closed in the finally block
        finally:
            connection.close()
                
                
                