class Person_Model:
    
    # Constructor
    def __init__(self, id_person, id_document_type_fk, doc_person, first_name_person, second_name_person, first_lastname_person, second_lastname_person, email_person, phone_person, address_person, state_person):
        self.__id_person = id_person
        self.__id_document_type_fk = id_document_type_fk
        self.__doc_person = doc_person
        self.__first_name_person = first_name_person
        self.__second_name_person = second_name_person
        self.__first_lastname_person = first_lastname_person
        self.__second_lastname_person = second_lastname_person
        self.__email_person = email_person
        self.__phone_person = phone_person
        self.__address_person = address_person
        self.__state_person = state_person
    
    # Getters
    def get_id_person(self):
        return self.__id_person
    
    def get_id_document_type_fk(self):
        return self.__id_document_type_fk
    
    def get_doc_person(self):
        return self.__doc_person
    
    def get_first_name_person(self):
        return self.__first_name_person
    
    def get_second_name_person(self):
        return self.__second_name_person
    
    def get_first_lastname_person(self):
        return self.__first_lastname_person
    
    def get_second_lastname_person(self):  
        return self.__second_lastname_person
    
    def get_email_person(self):
        return self.__email_person
    
    def get_phone_person(self):
        return self.__phone_person
    
    def get_address_person(self):
        return self.__address_person
    
    def get_state_person(self):
        return self.__state_person
    
    # Setters

    def set_id_person(self, id_person):
        self.__id_person = id_person

    def set_id_document_type_fk(self, id_document_type_fk):
        self.__id_document_type_fk = id_document_type_fk
    
    def set_doc_person(self, doc_person):
        self.__doc_person = doc_person

    def set_first_name_person(self, first_name_person):
        self.__first_name_person = first_name_person

    def set_second_name_person(self, second_name_person):
        self.__second_name_person = second_name_person

    def set_first_lastname_person(self, first_lastname_person):
        self.__first_lastname_person = first_lastname_person
    
    def set_second_lastname_person(self, second_lastname_person):
        self.__second_lastname_person = second_lastname_person
    
    def set_email_person(self, email_person):
        self.__email_person = email_person

    def set_phone_person(self, phone_person):
        self.__phone_person = phone_person
    
    def set_address_person(self, address_person):
        self.__address_person = address_person
    
    def set_state_person(self, state_person):
        self.__state_person = state_person

    # Method to convert the object to a dictionary
    def to_dict(self):
        return {
            "id_person": self.__id_person,
            "id_document_type_fk": self.__id_document_type_fk,
            "doc_person": self.__doc_person,
            "first_name_person": self.__first_name_person,
            "second_name_person": self.__second_name_person,
            "first_lastname_person": self.__first_lastname_person,
            "second_lastname_person": self.__second_lastname_person,
            "email_person": self.__email_person,
            "phone_person": self.__phone_person,
            "address_person": self.__address_person,
            "state_person": self.__state_person
        }



