class Sale_Model:

    # Constructor
    def __init__(self, id_sale, id_order_fk, date_sale, total_sale, type_sale, state_sale = True):
        self.__id_sale = id_sale
        self.__id_order_fk = id_order_fk
        self.__date_sale = date_sale
        self.__total_sale = total_sale
        self.__type_sale = type_sale
        self.__state_sale = state_sale
    
    # Getters
    def get_id_sale(self):
        return self.__id_sale
    
    def get_id_order_fk(self):
        return self.__id_order_fk
    
    def get_date_sale(self):
        return self.__date_sale
    
    def get_total_sale(self):
        return self.__total_sale
    
    def get_type_sale(self):
        return self.__type_sale
    
    def get_state_sale(self):
        return self.__state_sale
    
    # Setters
    def set_id_sale(self, id_sale):
        self.__id_sale = id_sale

    def set_id_order_fk(self, id_order_fk):
        self.__id_order_fk = id_order_fk
    
    def set_date_sale(self, date_sale):
        self.__date_sale = date_sale

    def set_total_sale(self, total_sale):
        self.__total_sale = total_sale

    def set_type_sale(self, type_sale):
        self.__type_sale = type_sale
    
    def set_state_sale(self, state_sale):
        self.__state_sale = state_sale
    
    # Method to convert the object to a dictionary
    def to_dict(self):
        return {
            "id_sale": self.__id_sale,
            "id_order_fk": self.__id_order_fk,
            "date_sale": self.__date_sale,
            "total_sale": self.__total_sale,
            "type_sale": self.__type_sale,
            "state_sale": self.__state_sale
        }
