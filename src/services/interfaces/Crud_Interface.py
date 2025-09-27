from abc import ABC, abstractmethod

class Crud_Interface(ABC):
    
    @abstractmethod
    def consult(cls):
        pass
    
    @abstractmethod
    def create(cls, data):
        pass

    @abstractmethod
    def consult_id(cls, id):
        pass

    @abstractmethod
    def update(cls, id, data):
        pass

    @abstractmethod
    def change_state(cls, id):
        pass