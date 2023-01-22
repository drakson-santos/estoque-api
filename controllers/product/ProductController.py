import uuid
from models.Product import Product
from repository.repository import Repository
from exceptions.api.NotFoundException import NotFoundException
from controllers.FileController import FileController
from repository.inMemoryRepository.inMemory import InMemoryRepository

class ProductController:

    def __init__(self, repository=InMemoryRepository()):
        self.repository = Repository(repository)

    def get_products(self, product_id=None):
        products = self.repository.get("products", product_id)

        if not products:
            custom_message = "Products not found"
            if product_id:
                custom_message = f"Product not found for id: {product_id}"
            raise NotFoundException(custom_message)

        return products

    def save_product(self, product_name, model, category, quantity, photo=None):
        if photo:
            fileController = FileController()
            photo = fileController.save_file(photo)

        id = str(uuid.uuid4())
        product = Product(id, product_name, model, category, quantity, photo)

        self.repository.save("products", product.__dict__)

        return id

    def update_product(self, product_id, product_name=None, model=None, category=None, quantity=None):
        product = self.get_products(product_id)
        if not product:
            custom_message = f"Product not found for id: {product_id}"
            raise NotFoundException(custom_message)

        product = Product(
            product["id"],
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
            product.category = category
        if quantity:
            product.quantity = quantity

        self.repository.update("products", product_id, product.__dict__)

        return product.id

    def delete_product(self, product_id):
        product = self.get_products(product_id)
        if not product:
            custom_message = f"Product not found for id: {product_id}"
            raise NotFoundException(custom_message)

        self.repository.delete("products", product_id)