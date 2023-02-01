class Model:

    def __init__(self,id, model_name):
        self.id = id
        self.name = model_name

    def to_json(self):
        return {'id': self.id, 'name': self.name}