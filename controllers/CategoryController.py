from models.Category import Category
from repository.repository import Repository
import uuid

class CategoryController:

    def get_category(self, category_id=None):
        repository = Repository()
        return repository.get("category", category_id)

    def save_category(self, category_name):
        id = str(uuid.uuid4())
        category = Category(id, category_name)

        repository = Repository()
        repository.save("category", category.__dict__)

    def update_category(self,category_id, category_name = None):
        category = self.get_category(category_id)
        if not category:
            return False
        
        category = Category(
            category["id"],
            category["category_name"]
        )

        if category.category_name:
            category.category_name = category_name
        print(category.category_name)
        
        repository = Repository()
        repository.update("category", category_id, category.__dict__)
    
    def delete_category(self, category_id):
        category = self.get_category(category_id)
        if not category:
            return False
        repository = Repository()
        repository.delete("category", category_id)
