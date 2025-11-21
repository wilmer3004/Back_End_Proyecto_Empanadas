class Report_Model:

    # Constructor
    def __init__(self, id_report, id_report_type_fk, id_user_fk, date_report, detail_report, state_report = True):
        self.__id_report = id_report
        self.__id_report_type_fk = id_report_type_fk
        self.__id_user_fk = id_user_fk
        self.__date_report = date_report
        self.__detail_report = detail_report
        self.__state_report = state_report

    # Getters
    def get_id_report(self):
        return self.__id_report
    
    def get_id_report_type_fk(self):
        return self.__id_report_type_fk
    
    def get_id_user_fk(self):
        return self.__id_user_fk
    
    def get_date_report(self):
        return self.__date_report
    
    def get_detail_report(self):
        return self.__detail_report
    
    def get_state_report(self):
        return self.__state_report
    
    # Setters
    def set_id_report(self, id_report):
        self.__id_report = id_report
    
    def set_id_report_type_fk(self, id_report_type_fk):
        self.__id_report_type_fk = id_report_type_fk
    
    def set_id_user_fk(self, id_user_fk):
        self.__id_user_fk = id_user_fk
    
    def set_date_report(self, date_report):
        self.__date_report = date_report

    def set_detail_report(self, detail_report):
        self.__detail_report = detail_report

    def set_state_report(self, state_report):
        self.__state_report = state_report
    
    # Method to convert the object to a dictionary
    def to_dict(self):
        return {
            "id_report": self.__id_report,
            "id_report_type_fk": self.__id_report_type_fk,
            "id_user_fk": self.__id_user_fk,
            "date_report": self.__date_report,
            "detail_report": self.__detail_report,
            "state_report": self.__state_report
        }