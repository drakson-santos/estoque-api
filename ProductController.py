from Product import Product
from repository import Repository

class ProductController:

    def get_products(self, product_id=None):
        repository = Repository()
        return repository.get("products", product_id)

    def save_product(self, product_name, model, category, quantity):
        product = Product(product_name, model, category, quantity)

        repository = Repository()
        repository.save("products", product.__dict__)

    def update_product(self, product_id, product_name=None, model=None, category=None, quantity=None):
        product = self.get_products(product_id)
        if not product:
            return False

        product = Product(
            product["product_name"],
            product["model"],
            product["category"],
            product["quantity"]
        )

        if product_name:
            product.product_name = product_name
        if model:
            product.model = model
        if category:
            product.quantity = category
        if quantity:
            product.quantity = quantity

        repository = Repository()
        repository.update("products", product_id, product.__dict__)

    def delete_product(self, product_id):
        product = self.get_products(product_id)
        if not product:
            return False
        repository = Repository()
        repository.delete("products", product_id)