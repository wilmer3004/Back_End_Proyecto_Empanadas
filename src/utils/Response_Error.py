class Response_Error(Exception):
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.status_code = status_code
        self.message = message
    
    def to_dict(self):
        return {"error": self.message, "code": self.status_code}