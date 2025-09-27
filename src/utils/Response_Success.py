class Response_Success:
    def __init__(self, data, status_code=200):
        self.data = data
        self.status_code = status_code

    def to_dict(self):
        return {"data": self.data, "code": self.status_code}