import unittest
from unittest.mock import MagicMock
from repositories.categoryRepository import CategoryRepositorySqlLite
from databases import IDatabase
from mocks import category_mock
from models import Category

class TestCategoryRepositorySqlLite(unittest.TestCase):

    def setUp(self):
        self.database = MagicMock(spec=IDatabase)
        self.category_repository = CategoryRepositorySqlLite(self.database)

    def test_create_table_if_not_exists(self):
        self.category_repository.create_table_if_not_exists()
        self.database.create_table_if_not_exists.assert_called_with("categories", "CREATE TABLE categories (id TEXT PRIMARY KEY,  name TEXT)")

    def test_create(self):
        category_name = category_mock["category_name"]

        category = self.category_repository.create(category_name)

        self.database.create.assert_called_once()
        self.assertIsInstance(category, Category)
        self.assertEqual(category.name, category_name)

    def test_get_all(self):
        categories = [
            Category("1", "name1"),
            Category("2", "name2")
        ]
        self.database.read.return_value = categories
        result = self.category_repository.get_all()
        self.database.read.assert_called_once_with("SELECT * FROM categories")
        self.assertListEqual(result, categories)

    def test_get_by_id(self):
        category = Category("1", "name")
        self.database.read.return_value = [category]
        result = self.category_repository.get_by_id("1")
        self.database.read.assert_called_once_with("SELECT * FROM categories WHERE id = ?", ("1",))
        self.assertEqual(result, category)

    def test_update(self):
        category = Category("1", "name")
        self.category_repository.update(category.id, name='new name')
        self.database.update.assert_called_once_with("UPDATE categories SET name = ? WHERE id = ?", ('new name', category.id))

    def test_delete(self):
        self.category_repository.delete("1")
        self.database.delete.assert_called_once_with("DELETE FROM categories WHERE id = ?", ("1",))

