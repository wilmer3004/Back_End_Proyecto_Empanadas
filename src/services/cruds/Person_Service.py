from interfaces import Crud_Interface

class Person_Service(Crud_Interface):
    def __init__(self, person_model):
        self.person_model = person_model

    def create(self, data):
        pass

    def read(self, id):
        pass

    def update(self, id, data):
        pass

    def change_state(self, id):
        pass