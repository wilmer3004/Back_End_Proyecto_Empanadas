# src/utils/Response_Error.py
class Response_Error:
    def __init__(self, message, code=500):
        self.message = message
        self.code = code

    def to_dict(self):
        return {
            "success": False,
            "error": self.message,
            "code": self.code
        }
