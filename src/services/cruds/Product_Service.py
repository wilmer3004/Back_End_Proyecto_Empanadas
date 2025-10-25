from src.services.interfaces.Crud_Interface import Crud_Interface
from src.models.cruds.Product_Model import Product_Model
from src.database.database import get_db_conecction

class Product_Service(Crud_Interface):

    # Consult all products
    @classmethod
    def consult(cls):
        try:
            connection = get_db_conecction()
            products = []
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM product')
                result_products = cursor.fetchall()
                for row in result_products:
                    product = Product_Model(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    products.append(product.to_dict())
                connection.commit()
            return products
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to retrieve products", "code": 500}
        finally:
            connection.close()

    # Create a new product
    @classmethod
    def create(cls, data):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql = '''INSERT INTO product (id_product_type, name_product, price_product, stock_product, detail_product) 
                         VALUES (%s, %s, %s, %s, %s)'''
                data_tuple = (data['id_product_type_fk'], data['name_product'], data['price_product'], data['stock_product'], data['detail_product'])
                cursor.execute(sql, data_tuple)
                connection.commit()
                return {"message": "Product created successfully"}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to create product", "code": 500}
        finally:
            connection.close()

    # Consult a product by ID
    @classmethod
    def consult_id(cls, id):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM product WHERE id_product = %s'
                cursor.execute(sql, (id,))
                row = cursor.fetchone()
                if row:
                    product = Product_Model(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    return product.to_dict()
                return {"error": "Product not found", "code": 404}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to retrieve product", "code": 500}
        finally:
            connection.close()

    # Update product details
    @classmethod
    def update(cls, id, data):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql = '''UPDATE product 
                         SET id_product_type = %s, name_product = %s, price_product = %s, stock_product = %s, detail_product = %s 
                         WHERE id_product = %s'''
                data_tuple = (
                    data['id_product_type_fk'],
                    data['name_product'],
                    data['price_product'],
                    data['stock_product'],
                    data['detail_product'],
                    id
                )
                cursor.execute(sql, data_tuple)
                connection.commit()
                if cursor.rowcount == 0:
                    return {"error": "Product not found", "code": 404}
                return {"message": "Product updated successfully"}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to update product", "code": 500}
        finally:
            connection.close()

    # Change product state (activate/deactivate)
    @classmethod
    def change_state(cls, id):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql_check = "SELECT state_product FROM product WHERE id_product = %s"
                cursor.execute(sql_check, (id,))
                row = cursor.fetchone()

                if not row:
                    return {"error": "Product not found", "code": 404}

                current_state = row[0]
                new_state = not current_state

                sql = "UPDATE product SET state_product = %s WHERE id_product = %s"
                cursor.execute(sql, (new_state, id))
                connection.commit()

                return {"message": "Product state changed successfully", "new_state": new_state}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to change product state", "code": 500}
        finally:
            connection.close()
