from abc import ABC, abstractmethod

class Crud_Interface(ABC):
    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def read(self, id):
        pass

    @abstractmethod
    def update(self, id, data):
        pass

    @abstractmethod
    def change_state(self, id):
        pass