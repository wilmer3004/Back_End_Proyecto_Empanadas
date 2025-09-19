class User_Emp_Model:
    # Constructor
    def __init__(self, id_user, id_rol_fk, id_person_fk, username_user, password_user, token_user, state_user):
        self.__id_user = id_user
        self.__id_rol_fk = id_rol_fk
        self.__id_person_fk = id_person_fk
        self.__username_user = username_user
        self.__password_user = password_user
        self.__token_user = token_user
        self.__state_user = state_user
    
    # Getters
    def get_id_user(self):
        return self.__id_user
    
    def get_id_rol_fk(self):
        return self.__id_rol_fk
    
    def get_id_person_fk(self):
        return self.__id_person_fk
    
    def get_user(self):
        return self.__user
    
    def get_password_user(self):
        return self.__password_user
    
    def get_token_user(self):
        return self.__token_user
    
    def get_state_user(self):
        return self.__state_user
    
    # Setters
    def set_id_user(self, id_user):
        self.__id_user = id_user

    def set_id_rol_fk(self, id_rol_fk):
        self.__id_rol_fk = id_rol_fk
    
    def set_id_person_fk(self, id_person_fk):
        self.__id_person_fk = id_person_fk
    
    def set_user(self, username_user):
        self.__username_user = username_user
    
    def set_password_user(self, password_user):
        self.__password_user = password_user
    
    def set_token_user(self, token_user):
        self.__token_user = token_user

    def set_state_user(self, state_user):
        self.__state_user = state_user
    
    # Method to convert the object to a dictionary
    def to_dict(self):
        return {
            "id_user": self.__id_user,
            "id_rol_fk": self.__id_rol_fk,
            "id_person_fk": self.__id_person_fk,
            "username_user": self.__username_user,
            "password_user": self.__password_user,
            "token_user": self.__token_user,
            "state_user": self.__state_user
        }
    



