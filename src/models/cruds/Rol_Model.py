class RoL_Model:
    # Constructor
    def __init__(self, id_rol, name_rol, state_rol):
        self.__id_rol = id_rol
        self.__name_rol = name_rol
        self.__state_rol = state_rol
    
    # Getters
    def get_id_rol(self):
        return self.__id_rol
    
    def get_name_rol(self):
        return self.__name_rol
    
    def get_state_rol(self):
        return self.__state_rol
    
    # Setters

    def set_id_rol(self, id_rol):
        self.__id_rol = id_rol

    def set_name_rol(self, name_rol):
        self.__name_rol = name_rol
    
    def set_state_rol(self, state_rol):
        self.__state_rol = state_rol
    
    # Method to convert the object to a dictionary
    def to_dict(self):
        return {
            "id_rol": self.__id_rol,
            "name_rol": self.__name_rol,
            "state_rol": self.__state_rol
        }