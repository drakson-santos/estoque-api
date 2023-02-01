from repositories import IRepository

class ModelController:

    def __init__(self, model_repository):
        self.model_repository: IRepository = model_repository

    def create_model(self, name):
        return self.model_repository.create(name)

    def get_model(self, id):
        return self.model_repository.read(id)

    def update_model(self, id, model_name):
        return self.model_repository.update(id, model_name)

    def delete_model(self, id):
        return self.model_repository.delete(id)

    def get_all_models(self):
        return self.model_repository.read()