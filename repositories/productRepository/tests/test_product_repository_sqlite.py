import unittest
from unittest.mock import MagicMock
from repositories.productRepository import ProductRepositorySqlLite
from databases import IDatabase

class TestProductRepositorySqlLite(unittest.TestCase):

    def setUp(self):
        self.database = MagicMock(spec=IDatabase)
        self.product_repository = ProductRepositorySqlLite(self.database)

    def test_create_table_if_not_exists(self):
        self.product_repository.create_table_if_not_exists()
        self.database.create_table_if_not_exists.assert_called_with("products", "CREATE TABLE products (id TEXT PRIMARY KEY, product_name TEXT)")

    def test_create(self):
        product_name = "test_product"
        self.product_repository.create(product_name)
        self.database.create.assert_called_once()