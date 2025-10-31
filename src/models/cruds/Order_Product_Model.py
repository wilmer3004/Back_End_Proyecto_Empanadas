class Order_Product_Model:
    
    # Constructor
    def __init__(self, id_order_prod_fk, id_product_fk, quantity_product = 0):
        self.__id_order_prod_fk = id_order_prod_fk
        self.__id_product_fk = id_product_fk
        self.__quantity_product = quantity_product
    
    # Getters
    def get_id_order_prod_fk(self):
        return self.__id_order_prod_fk
    
    def get_id_product_fk(self):
        return self.__id_product_fk
    
    def get_quantity_product(self):
        return self.__quantity_product
    
    # Setters
    def set_id_order_prod_fk(self, id_order_prod_fk):
        self.__id_order_prod_fk = id_order_prod_fk
    
    def set_id_product_fk(self, id_product_fk):
        self.__id_product_fk = id_product_fk
    
    def set_quantity_product(self, quantity_product):
        self.__quantity_product = quantity_product
    
    # Method to convert the object to a dictionary
    def to_dict(self):
        return {
            "id_order_prod_fk": self.__id_order_prod_fk,
            "id_product_fk": self.__id_product_fk,
            "quantity_product": self.__quantity_product
        }
    
