from src.services.interfaces.Crud_Interface import Crud_Interface
from src.models.cruds.Customer_Model import Customer_Model
from src.database.database import get_db_conecction

class Customer_Service(Crud_Interface):

    # Get all customers
    @classmethod
    def consult(cls):
        try:
            connection = get_db_conecction()
            customers = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM customer")
                result_customer = cursor.fetchall()
                for row in result_customer:
                    customer = Customer_Model(row[0], row[1], row[2], row[3], row[4])
                    customers.append(customer.to_dict())
            connection.commit()
            return customers
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to retrieve customers", "code": 500}
        finally:
            connection.close()

    # Create new customer
    @classmethod
    def create(cls, data):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql = """
                    INSERT INTO customer (id_user_fk, id_type_customer_fk, customer_details)
                    VALUES (%s, %s, %s)
                """
                data_tuple = (
                    data["id_user_fk"],
                    data["id_type_customer_fk"],
                    data["customer_detail"]
                )
                cursor.execute(sql, data_tuple)
                connection.commit()
                return {"message": "Customer created successfully"}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to create customer", "code": 500}
        finally:
            connection.close()

    # Get customer by ID
    @classmethod
    def consult_id(cls, id):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM customer WHERE id_customer = %s", (id,))
                row = cursor.fetchone()
                if row:
                    customer = Customer_Model(row[0], row[1], row[2], row[3], row[4])
                    return customer.to_dict()
                return {"error": "Customer not found", "code": 404}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to retrieve customer", "code": 500}
        finally:
            connection.close()

    # Update customer
    @classmethod
    def update(cls, id, data):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                sql = """
                    UPDATE customer
                    SET id_user_fk = %s, id_type_customer_fk = %s, customer_details = %s
                    WHERE id_customer = %s
                """
                data_tuple = (
                    data["id_user_fk"],
                    data["id_type_customer_fk"],
                    data["customer_detail"],
                    id
                )
                cursor.execute(sql, data_tuple)
                connection.commit()
                if cursor.rowcount == 0:
                    return {"error": "Customer not found", "code": 404}
                return {"message": "Customer updated successfully"}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to update customer", "code": 500}
        finally:
            connection.close()

    # Change customer state (active/inactive)
    @classmethod
    def change_state(cls, id):
        try:
            connection = get_db_conecction()
            with connection.cursor() as cursor:
                cursor.execute("SELECT state_customer FROM customer WHERE id_customer = %s", (id,))
                row = cursor.fetchone()
                if not row:
                    return {"error": "Customer not found", "code": 404}
                current_state = row[0]
                new_state = not current_state
                cursor.execute("UPDATE customer SET state_customer = %s WHERE id_customer = %s", (new_state, id))
                connection.commit()
                return {"message": "Customer state changed successfully", "new_state": new_state}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": "Failed to change customer state", "code": 500}
        finally:
            connection.close()
