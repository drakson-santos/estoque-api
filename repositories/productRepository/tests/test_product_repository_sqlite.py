import unittest
from unittest.mock import MagicMock
from repositories.productRepository import ProductRepositorySqlLite
from databases import IDatabase
from mocks import product_mock

class TestProductRepositorySqlLite(unittest.TestCase):

    def setUp(self):
        self.database = MagicMock(spec=IDatabase)
        self.product_repository = ProductRepositorySqlLite(self.database)

    def test_create_table_if_not_exists(self):
        self.product_repository.create_table_if_not_exists()
        self.database.create_table_if_not_exists.assert_called_with("products", "CREATE TABLE products (id TEXT PRIMARY KEY,  product_model TEXT, product_category TEXT, product_quantity INTEGER, product_sale_price FLOAT, product_purchase_price FLOAT, product_photo TEXT)")

    def test_create(self):
        product_name = product_mock["product_name"]
        product_model = product_mock["model"]
        product_category = product_mock["category"]
        product_quantity = product_mock["quantity"]
        product_sale_price = product_mock["sale_price"]
        product_purchase_price = product_mock["purchase_price"]
        product_photo = product_mock["photo"]

        self.product_repository.create(
            product_name,
            product_model,
            product_category,
            product_quantity,
            product_sale_price,
            product_purchase_price,
            product_photo
        )
        self.database.create.assert_called_once()