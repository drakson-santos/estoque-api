from repositories import IRepository

class CategoryController:

    def __init__(self, category_repository):
        self.category_repository: IRepository = category_repository

    def create_category(self, name):
        return self.category_repository.create(name)

    def get_category(self, id):
        return self.category_repository.read(id)

    def update_category(self, id, category_name):
        return self.category_repository.update(id, category_name)

    def delete_category(self, id):
        return self.category_repository.delete(id)

    def get_all_categories(self):
        return self.category_repository.read()