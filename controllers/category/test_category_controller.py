from controllers.category.CategoryController import CategoryController
from mocks.category import category_mock

from unittest import TestCase

class CategoryControllerSaveCategory(TestCase):

    def test_it_should_be_possible_to_create_category(self):
        categoryController = CategoryController()
        category_name = category_mock["category_name"]
        category_id = categoryController.save_category(category_name)
        self.assertIsInstance(category_id, str)

    def test_it_should_not_be_possible_to_create_category_without_sending_data(self):
        categoryController = CategoryController()
        with self.assertRaises(Exception):
            categoryController.save_category()