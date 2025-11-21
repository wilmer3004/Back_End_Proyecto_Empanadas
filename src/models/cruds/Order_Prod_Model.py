class Order_Prod_Model:
    # Constructor
    def __init__(self, id_order_prod, id_customer_fk, detail_order, date_order, state_order):
        self.__id_order_prod = id_order_prod
        self.__id_customer_fk = id_customer_fk
        self.__detail_order = detail_order
        self.__date_order = date_order
        self.__state_order = state_order
        self.products = [] 
    
    # Getters
    def get_id_order_prod(self):
        return self.__id_order_prod
    
    def get_id_customer_fk(self):
        return self.__id_customer_fk
    
    def get_detail_order(self):
        return self.__detail_order
    
    def get_date_order(self):
        return self.__date_order
    
    def get_state_order(self):
        return self.__state_order
    
    def get_products(self):
        return self.products
    
    # Setters
    def set_id_order_prod(self, id_order_prod):
        self.__id_order_prod = id_order_prod
    
    def set_id_customer_fk(self, id_customer_fk):
        self.__id_customer_fk = id_customer_fk
    
    def set_detail_order(self, detail_order):
        self.__detail_order = detail_order
    
    def set_date_order(self, date_order):
        self.__date_order = date_order
    
    def set_state_order(self, state_order):
        self.__state_order = state_order
        
    def set_products(self, products):
        self.products = products
    
    # Method to convert the object to a dictionary
    def to_dict(self):
        return {
            "id_order_prod": self.__id_order_prod,
            "id_customer_fk": self.__id_customer_fk,
            "detail_order": self.__detail_order,
            "date_order": self.__date_order,
            "state_order": self.__state_order,
            "products": self.products
        }
    