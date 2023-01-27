from repositories import IRepository

class ProductController:

    def __init__(self, product_repository):
        self.product_repository: IRepository = product_repository

    def create_product(self, name, model, category,
            quantity, sale_price, purchase_price, photo
    ):
        return self.product_repository.create(name, model, category,
            quantity, sale_price, purchase_price, photo
        )

    def get_product(self, id):
        return self.product_repository.read(id)

    def update_product(self, id, product_name):
        return self.product_repository.update(id, product_name)

    def delete_product(self, id):
        return self.product_repository.delete(id)

    def get_all_products(self):
        return self.product_repository.read()