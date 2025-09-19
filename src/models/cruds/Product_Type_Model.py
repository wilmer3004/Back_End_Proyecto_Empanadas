class Product_Type_Model:
    
    # Constructor
    def __init__(self, id_product_type, name_product_type, detail_product_type, state_product_type):
        self.__id_product_type = id_product_type
        self.__name_product_type = name_product_type
        self.__detail_product_type = detail_product_type
        self.__state_product_type = state_product_type
    
    # Getters
    def get_id_product_type(self):
        return self.__id_product_type
    
    def get_name_product_type(self):
        return self.__name_product_type
    
    def get_detail_product_type(self):
        return self.__detail_product_type
    
    def get_state_product_type(self):
        return self.__state_product_type
    
    # Setters

    def set_id_product_type(self, id_product_type):
        self.__id_product_type = id_product_type

    def set_name_product_type(self, name_product_type):
        self.__name_product_type = name_product_type
    
    def set_detail_product_type(self, detail_product_type):
        self.__detail_product_type = detail_product_type

    def set_state_product_type(self, state_product_type):
        self.__state_product_type = state_product_type
    
    # Method to convert the object to a dictionary
    def to_dict(self):
        return {
            "id_product_type": self.__id_product_type,
            "name_product_type": self.__name_product_type,
            "detail_product_type": self.__detail_product_type,
            "state_product_type": self.__state_product_type
        }

