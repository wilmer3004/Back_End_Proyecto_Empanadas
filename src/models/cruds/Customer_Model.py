class Customer_Model:
    # Constructor
    def __init__(self, id_customer, id_user_fk, customer_detail, state_customer):
        self.__id_customer = id_customer
        self.__id_user_fk = id_user_fk
        self.__customer_detail = customer_detail
        self.__state_customer = state_customer
    
    # Getters
    def get_id_customer(self):
        return self.__id_customer
    
    def get_id_user_fk(self):
        return self.__id_user_fk
    
    def get_customer_detail(self):
        return self.__customer_detail
    
    def get_state_customer(self):
        return self.__state_customer
    
    # Setters
    def set_id_customer(self, id_customer):
        self.__id_customer = id_customer

    def set_id_user_fk(self, id_user_fk):
        self.__id_user_fk = id_user_fk

    def set_customer_detail(self, customer_detail):
        self.__customer_detail = customer_detail
    
    def set_state_customer(self, state_customer):
        self.__state_customer = state_customer

    # Method to convert the object to a dictionary
    def to_dict(self):
        return {
            "id_customer": self.__id_customer,
            "id_user_fk": self.__id_user_fk,
            "customer_detail": self.__customer_detail,
            "state_customer": self.__state_customer
        }
