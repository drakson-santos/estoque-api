from controllers.model.ModelController import ModelController
from mocks.model import model_mock

from unittest import TestCase

class ModelControllerSaveCategory(TestCase):

    def test_it_should_be_possible_to_create_model(self):
        modelController = ModelController()
        model_name = model_mock["model_name"]
        model_id = modelController.save_model(model_name)
        self.assertIsInstance(model_id, str)

    def test_it_should_not_be_possible_to_create_model_without_sending_data(self):
        modelController = ModelController()
        with self.assertRaises(Exception):
            modelController.save_model()