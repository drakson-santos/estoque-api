import unittest
from unittest.mock import MagicMock
from repositories import IRepository
from controllers import CategoryController
from mocks import category_mock

class TestCategoryController(unittest.TestCase):

    def setUp(self):
        self.category_repository = MagicMock(spec=IRepository)
        self.category_controller = CategoryController(self.category_repository)

    def test_create_category(self):
        category_name = category_mock["category_name"]
        self.category_controller.create_category(category_name)
        self.category_repository.create.assert_called_once_with(category_name)

    def test_get_category(self):
        category_id = 1
        self.category_controller.get_category(category_id)
        self.category_repository.read.assert_called_once_with(category_id)

    def test_get_all_categories(self):
        self.category_controller.get_all_categories()
        self.category_repository.read.assert_called_once_with()

    def test_update_category(self):
        category_id = 1
        category_name = "New Category Name"
        self.category_controller.update_category(category_id, category_name)
        self.category_repository.update.assert_called_once_with(category_id, category_name)

    def test_delete_category(self):
        category_id = 1
        self.category_controller.delete_category(category_id)
        self.category_repository.delete.assert_called_once_with(category_id)