import uuid
from models.Category import Category
from repository.repository import Repository
from exceptions.api.NotFoundException import NotFoundException

class CategoryController:

    def get_category(self, category_id=None):
        repository = Repository()
        category = repository.get("category", category_id)

        if not category:
            custom_message = "Category not found"
            if category_id:
                custom_message = f"Category not found for id:{category_id}"
            raise NotFoundException(custom_message)
        
        return category 

    def save_category(self, category_name):
        id = str(uuid.uuid4())
        category = Category(id, category_name)

        repository = Repository()
        repository.save("category", category.__dict__)
        return id

    def update_category(self,category_id, category_name = None):
        category = self.get_category(category_id)
        if not category:
            custom_message = f"Category not found for id: {category_id}"
            raise NotFoundException(custom_message)
        
        category = Category(
            category["id"],
            category["category_name"]
        )

        if category.category_name:
            category.category_name = category_name
        
        repository = Repository()
        repository.update("category", category_id, category.__dict__)

        return category.id
    
    def delete_category(self, category_id):
        category = self.get_category(category_id)
        if not category:
            custom_message = f"Category not foundo for id: {category_id}"
            raise NotFoundException(custom_message)

        repository = Repository()
        repository.delete("category", category_id)
