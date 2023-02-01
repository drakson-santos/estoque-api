import unittest
from unittest.mock import MagicMock
from repositories.modelRepository import ModelRepositorySqlLite
from databases import IDatabase
from mocks import model_mock
from models import Model

class TestModelRepositorySqlLite(unittest.TestCase):

    def setUp(self):
        self.database = MagicMock(spec=IDatabase)
        self.model_repository = ModelRepositorySqlLite(self.database)

    def test_create_table_if_not_exists(self):
        self.model_repository.create_table_if_not_exists()
        self.database.create_table_if_not_exists.assert_called_with("models", "CREATE TABLE models (id TEXT PRIMARY KEY,  name TEXT)")

    def test_create(self):
        model_name = model_mock["model_name"]

        model = self.model_repository.create(model_name)

        self.database.create.assert_called_once()
        self.assertIsInstance(model, Model)
        self.assertEqual(model.name, model_name)

    def test_get_all(self):
        models = [
            Model("1", "name1"),
            Model("2", "name2")
        ]
        self.database.read.return_value = models
        result = self.model_repository.get_all()
        self.database.read.assert_called_once_with("SELECT * FROM models")
        self.assertListEqual(result, models)

    def test_get_by_id(self):
        model = Model("1", "name")
        self.database.read.return_value = [model]
        result = self.model_repository.get_by_id("1")
        self.database.read.assert_called_once_with("SELECT * FROM models WHERE id = ?", ("1",))
        self.assertEqual(result, model)

    def test_update(self):
        model = Model("1", "name")
        self.model_repository.update(model.id, name='new name')
        self.database.update.assert_called_once_with("UPDATE models SET name = ? WHERE id = ?", ('new name', model.id))

    def test_delete(self):
        self.model_repository.delete("1")
        self.database.delete.assert_called_once_with("DELETE FROM models WHERE id = ?", ("1",))

