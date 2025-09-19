class Order_Product_Model:
    
    # Constructor
    def __init__(self, id_order_prod_fk, id_product_fk):
        self.__id_order_prod_fk = id_order_prod_fk
        self.__id_product_fk = id_product_fk
    
    # Getters
    def get_id_order_prod_fk(self):
        return self.__id_order_prod_fk
    
    def get_id_product_fk(self):
        return self.__id_product_fk
    
    # Setters
    def set_id_order_prod_fk(self, id_order_prod_fk):
        self.__id_order_prod_fk = id_order_prod_fk
    
    def set_id_product_fk(self, id_product_fk):
        self.__id_product_fk = id_product_fk
    
    # Method to convert the object to a dictionary
    def to_dict(self):
        return {
            "id_order_prod_fk": self.__id_order_prod_fk,
            "id_product_fk": self.__id_product_fk
        }
    
