class Auth_Model:
    # Constructor
    def __init__(self, id_user, id_rol_fk, id_person_fk, user_name, password_user, token_user, state_user):
        self.__id_user = id_user
        self.__id_rol_fk = id_rol_fk
        self.__id_person_fk = id_person_fk
        self.__user_name = user_name
        self.__password_user = password_user
        self.__token_user = token_user
        self.__state_user = state_user

    # to dict method
    def to_dict(self):
        return {
            "id_user": self.__id_user,
            "id_rol_fk": self.__id_rol_fk,
            "id_person_fk": self.__id_person_fk,
            "user_name": self.__user_name,
            "password_user": self.__password_user,
            "token_user": self.__token_user,
            "state_user": self.__state_user
        }