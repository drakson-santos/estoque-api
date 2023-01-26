import unittest
from unittest.mock import MagicMock
from repositories import IRepository
from controllers import ProductController

class TestProductController(unittest.TestCase):

    def setUp(self):
        self.product_repository = MagicMock(spec=IRepository)
        self.product_controller = ProductController(self.product_repository)

    def test_create_product(self):
        product_name = "test_product"
        self.product_controller.create_product(product_name)
        self.product_repository.create.assert_called_once_with(product_name)