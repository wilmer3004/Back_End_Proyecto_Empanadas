from src.services.interfaces.Crud_Interface import Crud_Interface
from src.models.cruds.Product_Type_Model import Product_Type_Model
from src.database.database import get_db_conecction

class Product_Type_Service(Crud_Interface):
    
    # Implementing the abstract method from Crud:Interface
    
    # Consult all product types
    @classmethod
    def consult(cls):
        # Imple
    