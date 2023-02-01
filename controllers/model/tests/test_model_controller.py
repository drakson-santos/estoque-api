import unittest
from unittest.mock import MagicMock
from repositories import IRepository
from controllers import ModelController
from mocks import model_mock

class TestModelController(unittest.TestCase):

    def setUp(self):
        self.model_repository = MagicMock(spec=IRepository)
        self.model_controller = ModelController(self.model_repository)

    def test_create_model(self):
        model_name = model_mock["model_name"]
        self.model_controller.create_model(model_name)
        self.model_repository.create.assert_called_once_with(model_name)

    def test_get_model(self):
        model_id = 1
        self.model_controller.get_model(model_id)
        self.model_repository.read.assert_called_once_with(model_id)

    def test_get_all_models(self):
        self.model_controller.get_all_models()
        self.model_repository.read.assert_called_once_with()

    def test_update_model(self):
        model_id = 1
        model_name = "New Model Name"
        self.model_controller.update_model(model_id, model_name)
        self.model_repository.update.assert_called_once_with(model_id, model_name)

    def test_delete_model(self):
        model_id = 1
        self.model_controller.delete_model(model_id)
        self.model_repository.delete.assert_called_once_with(model_id)