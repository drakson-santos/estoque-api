from unittest import TestCase
from controllers.category.CategoryController import CategoryController
from mocks.category import category_mock
from exceptions.api.NotFoundException import NotFoundException
from repository.inMemoryRepository.inMemory import InMemoryRepository

class CategoryControllerGetCategory(TestCase):

    def test_it_should_be_possible_to_get_categories(self):
        categoryController = CategoryController(InMemoryRepository())
        category_name = category_mock["category_name"]
        categoryController.save_category(category_name)

        categories = categoryController.get_category()

        self.assertIsInstance(categories, list)
        self.assertIn("id", categories[0])
        self.assertIn("category_name", categories[0])

    def test_it_should_be_possible_to_get_category_by_id(self):
        categoryController = CategoryController(InMemoryRepository())
        category_name = category_mock["category_name"]
        category_id = categoryController.save_category(category_name)

        category = categoryController.get_category(category_id)

        self.assertIsInstance(category, dict)
        self.assertIn("id", category)
        self.assertIn("category_name", category)

    def test_it_should_not_be_possible_to_fetch_category_with_invalid_id(self):
        categoryController = CategoryController(InMemoryRepository())
        invalid_category_id = "ERROR"

        with self.assertRaises(NotFoundException):
            categoryController.get_category(invalid_category_id)

class CategoryControllerSaveCategory(TestCase):

    def test_it_should_be_possible_to_create_category(self):
        categoryController = CategoryController(InMemoryRepository())
        category_name = category_mock["category_name"]

        category_id = categoryController.save_category(category_name)

        self.assertIsInstance(category_id, str)

    def test_it_should_not_be_possible_to_create_category_without_sending_data(self):
        categoryController = CategoryController(InMemoryRepository())

        with self.assertRaises(Exception):
            categoryController.save_category()

class CategoryControllerUpdateCategory(TestCase):

    def test_it_should_be_possible_to_update_category(self):
        categoryController = CategoryController(InMemoryRepository())
        category_name = category_mock["category_name"]
        category_id = categoryController.save_category(category_name)

        old_category = categoryController.get_category(category_id)

        after_category_id = categoryController.update_category(category_id, "category mock updated")
        current_category = categoryController.get_category(after_category_id)

        self.assertIsInstance(current_category, dict)
        self.assertIn("id", current_category)
        self.assertIn("category_name", current_category)
        self.assertEqual(old_category["id"], current_category["id"])
        self.assertNotEqual(old_category["category_name"], current_category["category_name"])

    def test_it_should_not_be_possible_to_update_category_with_invalid_id(self):
        categoryController = CategoryController(InMemoryRepository())

        with self.assertRaises(NotFoundException):
            categoryController.update_category("ID INVALID")

class CategoryControllerDeleteCategory(TestCase):

    def test_it_should_be_possible_to_delete_category(self):
        categoryController = CategoryController(InMemoryRepository())
        category_name = category_mock["category_name"]
        category_id = categoryController.save_category(category_name)

        categoryController.delete_category(category_id)

        with self.assertRaises(NotFoundException):
            categoryController.get_category(category_id)

    def test_it_should_not_be_possible_to_delete_category_with_invalid_id(self):
        categoryController = CategoryController(InMemoryRepository())

        with self.assertRaises(NotFoundException):
            categoryController.delete_category("ID INVALID")
