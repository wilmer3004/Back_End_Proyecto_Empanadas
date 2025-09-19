class Product_Model:

    # Constructor
    def __init__(self, id_product, id_product_type_fk, name_product, price_product,stock_product, detail_product,  state_product):
        self.__id_product = id_product
        self.__id_product_type_fk = id_product_type_fk
        self.__name_product = name_product
        self.__price_product = price_product
        self.__stock_product = stock_product
        self.__detail_product = detail_product
        self.__state_product = state_product
    
    # Getters
    def get_id_product(self):
        return self.__id_product
    
    def get_id_product_type_fk(self):
        return self.__id_product_type_fk
    
    def get_name_product(self):
        return self.__name_product
    
    def get_price_product(self):
        return self.__price_product
    
    def get_stock_product(self):
        return self.__stock_product
    
    def get_detail_product(self):
        return self.__detail_product
    
    def get_state_product(self):
        return self.__state_product
    
    # Setters
    def set_id_product(self, id_product):
        self.__id_product = id_product
    
    def set_id_product_type_fk(self, id_product_type_fk):
        self.__id_product_type_fk = id_product_type_fk
    
    def set_name_product(self, name_product):
        self.__name_product = name_product
    
    def set_price_product(self, price_product):
        self.__price_product = price_product
    
    def set_stock_product(self, stock_product):
        self.__stock_product = stock_product
    
    def set_detail_product(self, detail_product):
        self.__detail_product = detail_product
    
    def set_state_product(self, state_product):
        self.__state_product = state_product
    
    # Method to convert the object to a dictionary
    def to_dict(self):
        return {
            "id_product": self.__id_product,
            "id_product_type_fk": self.__id_product_type_fk,
            "name_product": self.__name_product,
            "price_product": self.__price_product,
            "stock_product": self.__stock_product,
            "detail_product": self.__detail_product,
            "state_product": self.__state_product
        }