class Document_type_Model:

    # Constructor
    def __init__(self, id_document_type, name_document_type, acronym_document_type, state_document_type):
        self.__id_document_type = id_document_type
        self.__name_document_type = name_document_type
        self.__acronym_document_type = acronym_document_type
        self.__state_document_type = state_document_type
    
    # Getters
    def get_id_document_type(self):
        return self.__id_document_type
    
    def get_name_document_type(self):
        return self.__name_document_type
    
    def get_acronym_document_type(self):
        return self.__acronym_document_type
    
    def get_state_document_type(self):
        return self.__state_document_type
    
    # Setters

    def set_id_document_type(self, id_document_type):
        self.__id_document_type = id_document_type

    def set_name_document_type(self, name_document_type):
        self.__name_document_type = name_document_type
    
    def set_acronym_document_type(self, acronym_document_type):
        self.__acronym_document_type = acronym_document_type
    
    def set_state_document_type(self, state_document_type):
        self.__state_document_type = state_document_type
    
    # Method to convert the object to a dictionary
    def to_dict(self):
        return {
            "id_document_type": self.__id_document_type,
            "name_document_type": self.__name_document_type,
            "acronym_document_type": self.__acronym_document_type,
            "state_document_type": self.__state_document_type
        }
