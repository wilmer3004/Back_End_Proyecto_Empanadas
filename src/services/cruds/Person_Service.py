from interfaces import Crud_Interface
from src.models.cruds.Person_Model import Person_Model
from src.database import get_db_conecction

class Person_Service(Crud_Interface):
    
    # Implementing the abstract methods from Crud_Interface
    # Consult all persons
    @classmethod
    def consult(cls):
        # Implement the logic to retrieve all persons from the database
        try:
            connection = get_db_conecction()
            people = []
        
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Person")
                result_person = cursor.fetchall()
                for row in result_person:
                    person = Person_Model(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                    people.append(person.to_dict())
                connection.commit()
            return people
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            connection.close()
    
    # Create a new person
    @classmethod
    def create(cls, data):
        pass
    
    @classmethod
    def consult_id(cls, id):
        pass

    @classmethod
    def update(cls, id, data):
        pass

    @classmethod
    def change_state(cls, id):
        pass