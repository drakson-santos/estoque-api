from unittest import TestCase
from controllers.model.ModelController import ModelController
from mocks.model import model_mock
from exceptions.api.NotFoundException import NotFoundException
from repository.inMemoryRepository.inMemory import InMemoryRepository

class ModelControllerGetModel(TestCase):

    def test_it_should_be_possible_to_get_models(self):
        modelController = ModelController(InMemoryRepository())
        model_name = model_mock["model_name"]
        modelController.save_model(model_name)

        models = modelController.get_model()

        self.assertIsInstance(models, list)
        self.assertIn("id", models[0])
        self.assertIn("model_name", models[0])

    def test_it_should_be_possible_to_get_model_by_id(self):
        modelController = ModelController(InMemoryRepository())
        model_name = model_mock["model_name"]
        model_id = modelController.save_model(model_name)

        model = modelController.get_model(model_id)

        self.assertIsInstance(model, dict)
        self.assertIn("id", model)
        self.assertIn("model_name", model)

    def test_it_should_not_be_possible_to_fetch_model_with_invalid_id(self):
        modelController = ModelController(InMemoryRepository())
        invalid_model_id = "ERROR"

        with self.assertRaises(NotFoundException):
            modelController.get_model(invalid_model_id)

class ModelControllerSaveModel(TestCase):

    def test_it_should_be_possible_to_create_model(self):
        modelController = ModelController(InMemoryRepository())
        model_name = model_mock["model_name"]
        model_id = modelController.save_model(model_name)
        self.assertIsInstance(model_id, str)

    def test_it_should_not_be_possible_to_create_model_without_sending_data(self):
        modelController = ModelController(InMemoryRepository())
        with self.assertRaises(Exception):
            modelController.save_model()

class ModelControllerUpdateModel(TestCase):

    def test_it_should_be_possible_to_update_model(self):
        modelController = ModelController(InMemoryRepository())
        model_name = model_mock["model_name"]
        model_id = modelController.save_model(model_name)

        old_model = modelController.get_model(model_id)

        after_model_id = modelController.update_model(model_id, "model mock updated")
        current_model = modelController.get_model(after_model_id)

        self.assertIsInstance(current_model, dict)
        self.assertIn("id", current_model)
        self.assertIn("model_name", current_model)
        self.assertEqual(old_model["id"], current_model["id"])
        self.assertNotEqual(old_model["model_name"], current_model["model_name"])

    def test_it_should_not_be_possible_to_update_model_with_invalid_id(self):
        modelController = ModelController(InMemoryRepository())

        with self.assertRaises(NotFoundException):
            modelController.update_model("ID INVALID")

class ModelControllerDeleteModel(TestCase):

    def test_it_should_be_possible_to_delete_model(self):
        modelController = ModelController(InMemoryRepository())
        model_name = model_mock["model_name"]
        model_id = modelController.save_model(model_name)

        modelController.delete_model(model_id)

        with self.assertRaises(NotFoundException):
            modelController.get_model(model_id)

    def test_it_should_not_be_possible_to_delete_model_with_invalid_id(self):
        modelController = ModelController(InMemoryRepository())

        with self.assertRaises(NotFoundException):
            modelController.delete_model("ID INVALID")