class Customer_Type_Model:

    # Constructor
    def __init__(self, id_customer_type, name_customer_type, detail_customer_type, state_customer_type = True):
        self.__id_customer_type = id_customer_type
        self.__name_customer_type = name_customer_type
        self.__detail_customer_type = detail_customer_type
        self.__state_customer_type = state_customer_type
    
    # Getters
    def get_id_customer_type(self):
        return self.__id_customer_type
    
    def get_name_customer_type(self):
        return self.__name_customer_type
    
    def get_detail_customer_type(self):
        return self.__detail_customer_type
    
    def get_state_customer_type(self):
        return self.__state_customer_type
    
    # Setters
    def set_id_customer_type(self, id_customer_type):
        self.__id_customer_type = id_customer_type
    
    def set_name_customer_type(self, name_customer_type):
        self.__name_customer_type = name_customer_type

    def set_detail_customer_type(self, detail_customer_type):
        self.__detail_customer_type = detail_customer_type
    
    def set_state_customer_type(self, state_customer_type):
        self.__state_customer_type = state_customer_type
    
    # Method to convert the object to a dictionary
    def to_dict(self):
        return {
            "id_customer_type": self.__id_customer_type,
            "name_customer_type": self.__name_customer_type,
            "detail_customer_type": self.__detail_customer_type,
            "state_customer_type": self.__state_customer_type
        }
    