import uuid
from models.Model import Model
from repository.repository import Repository
from exceptions.api.NotFoundException import NotFoundException

class ModelController:

    def get_model(self, model_id=None):
        repository = Repository()
        model = repository.get("model", model_id)

        if not model:
            custom_message = "Model not found"
            if model_id:
                custom_message = f"Model not found for id:{model_id}"
            raise NotFoundException(custom_message)
        
        return model 

    def save_model(self, model_name):
        id = str(uuid.uuid4())
        model = Model(id, model_name)

        repository = Repository()
        repository.save("model", model.__dict__)
        return id

    def update_model(self,model_id, model_name = None):
        model = self.get_model(model_id)
        if not model:
            custom_message = f"Model not found for id: {model_id}"
            raise NotFoundException(custom_message)
        
        model = Model(
            model["id"],
            model["model_name"]
        )

        if model.model_name:
            model.model_name = model_name
        
        repository = Repository()
        repository.update("model", model_id, model.__dict__)

        return model.id
    
    def delete_model(self, model_id):
        model = self.get_model(model_id)
        if not model:
            custom_message = f"Model not foundo for id: {model_id}"
            raise NotFoundException(custom_message)

        repository = Repository()
        repository.delete("model", model_id)
