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
        product_name = product_mock["test_product"]
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
        self.product_repository.create.assert_called_once_with(product_name)