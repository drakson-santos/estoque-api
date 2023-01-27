import unittest
from unittest.mock import MagicMock
from repositories import IRepository
from controllers import ProductController
from mocks import product_mock

class TestProductController(unittest.TestCase):

    def setUp(self):
        self.product_repository = MagicMock(spec=IRepository)
        self.product_controller = ProductController(self.product_repository)

    def test_create_product(self):
        product_name = product_mock["product_name"]
        product_model = product_mock["model"]
        product_category = product_mock["category"]
        product_quantity = product_mock["quantity"]
        product_sale_price = product_mock["sale_price"]
        product_purchase_price = product_mock["purchase_price"]
        product_photo = product_mock["photo"]

        self.product_controller.create_product(
            product_name,
            product_model,
            product_category,
            product_quantity,
            product_sale_price,
            product_purchase_price,
            product_photo
        )
        self.product_repository.create.assert_called_once_with(
            product_name,
            product_model,
            product_category,
            product_quantity,
            product_sale_price,
            product_purchase_price,
            product_photo
        )

    def test_get_product(self):
        product_id = 1
        self.product_controller.get_product(product_id)
        self.product_repository.read.assert_called_once_with(product_id)

    def test_get_all_products(self):
        self.product_controller.get_all_products()
        self.product_repository.read.assert_called_once_with()

    def test_update_product(self):
        product_id = 1
        product_name = "New Product Name"
        self.product_controller.update_product(product_id, product_name)
        self.product_repository.update.assert_called_once_with(product_id, product_name)

    def test_delete_product(self):
        product_id = 1
        self.product_controller.delete_product(product_id)
        self.product_repository.delete.assert_called_once_with(product_id)