class Report_Type_Model:

# Constructor
    def __init__(self, id_report_type, name_report_type, detail_report_type, state_report_type= True):
        self.__id_report_type = id_report_type
        self.__name_report_type = name_report_type
        self.__detail_report_type = detail_report_type
        self.__state_report_type = state_report_type
    
# Getters
    def get_id_report_type(self):
        return self.__id_report_type
    
    def get_name_report_type(self):
        return self.__name_report_type
    
    def get_detail_report_type(self):
        return self.__detail_report_type
    
    def get_state_report_type(self):
        return self.__state_report_type
    
# Setters
    def set_id_report_type(self, id_report_type):
        self.__id_report_type = id_report_type

    def set_name_report_type(self, name_report_type):
        self.__name_report_type = name_report_type
    
    def set_detail_report_type(self, detail_report_type):
        self.__detail_report_type = detail_report_type
    
    def set_state_report_type(self, state_report_type):
        self.__state_report_type = state_report_type
    
# Method to convert the object to a dictionary
    def to_dict(self):
        return {
            "id_report_type": self.__id_report_type,
            "name_report_type": self.__name_report_type,
            "detail_report_type": self.__detail_report_type,
            "state_report_type": self.__state_report_type
        }