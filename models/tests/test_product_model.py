from unittest import TestCase
from models.Product import Product
from mocks.product import product_mock

class ProductModel(TestCase):

    def test_it_should_be_possible_to_instance_product_model(self):
        product_mock_id = "PRODUCT_ID"
        Product(
            product_mock_id,
            product_mock["product_name"],
            product_mock["model"],
            product_mock["category"],
            product_mock["quantity"],
            product_mock["sale_price"],
            product_mock["purchase_price"],
            photo=product_mock["photo"],
        )
