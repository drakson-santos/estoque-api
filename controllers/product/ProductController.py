from models.Product import Product
from models.UniqueId import UniqueId
from repository.repository import Repository
from exceptions.api.NotFoundException import NotFoundException
from controllers.FileController import FileController
from repository.baseRepository import BaseRepository

class ProductController:

    def __init__(self, repository: BaseRepository):
        self.repository = Repository(repository)

    def get_products(self, product_id=None):
        products = self.repository.get("products", product_id)

        if not products:
            custom_message = "Products not found"
            if product_id:
                custom_message = f"Product not found for id: {product_id}"
            raise NotFoundException(custom_message)

        return products

    def save_product(self, product_name, model, category, quantity, sale_price, purchase_price, photo=None):
        if photo:
            fileController = FileController()
            photo = fileController.save_file(photo)

        id = UniqueId.get_unique_id()
        product = Product(id, product_name, model, category, quantity, sale_price, purchase_price, photo)

        self.repository.save("products", product.__dict__)

        return id

    def update_product(self, product_id, product_name=None, model=None, category=None, sale_price=None, purchase_price=None, quantity=None):
        product = self.get_products(product_id)
        if not product:
            custom_message = f"Product not found for id: {product_id}"
            raise NotFoundException(custom_message)

        product = Product(
            product["id"],
            product["product_name"],
            product["model"],
            product["category"],
            product["quantity"],
            product["sale_price"],
            product["purchase_price"],
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