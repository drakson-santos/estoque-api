from unittest import TestCase
from controllers.product.ProductController import ProductController
from mocks.product import product_mock
from exceptions.api.NotFoundException import NotFoundException

class ProductControllerGetProduct(TestCase):

    def test_it_should_be_possible_to_get_products(self):
        productController = ProductController()
        product_name = product_mock["product_name"]
        model = product_mock["model"]
        category = product_mock["category"]
        quantity = product_mock["quantity"]
        sale_price = product_mock["sale_price"]
        purchase_price = product_mock["purchase_price"]
        productController.save_product(product_name, model, category, quantity, sale_price, purchase_price)

        products = productController.get_products()

        self.assertIsInstance(products, list)
        self.assertIn("id", products[0])
        self.assertIn("model", products[0])
        self.assertIn("category", products[0])
        self.assertIn("quantity", products[0])

    def test_it_should_be_possible_to_get_product_by_id(self):
        productController = ProductController()
        product_name = product_mock["product_name"]
        model = product_mock["model"]
        category = product_mock["category"]
        quantity = product_mock["quantity"]
        sale_price = product_mock["sale_price"]
        purchase_price = product_mock["purchase_price"]
        product_id = productController.save_product(product_name, model, category, sale_price, purchase_price, quantity)

        product = productController.get_products(product_id)

        self.assertIsInstance(product, dict)
        self.assertIn("id", product)
        self.assertIn("model", product)
        self.assertIn("category", product)
        self.assertIn("quantity", product)
        self.assertIn("sale_price", product)
        self.assertIn("purchase_price", product)

    def test_it_should_not_be_possible_to_fetch_product_with_invalid_id(self):
        productController = ProductController()
        invalid_product_id = "ERROR"

        with self.assertRaises(NotFoundException):
            productController.get_products(invalid_product_id)

class ProductControllerSaveProduct(TestCase):

    def test_it_should_be_possible_to_create_product(self):
        productController = ProductController()
        product_name = product_mock["product_name"]
        model = product_mock["model"]
        category = product_mock["category"]
        quantity = product_mock["quantity"]
        sale_price = product_mock["sale_price"]
        purchase_price = product_mock["purchase_price"]

        product_id = productController.save_product(product_name, model, category, sale_price, purchase_price, quantity)
        self.assertIsInstance(product_id, str)

    def test_it_should_not_be_possible_to_create_product_without_sending_data(self):
        productController = ProductController()

        with self.assertRaises(Exception):
            productController.save_product()

class ProductControllerUpdateProduct(TestCase):

    def test_it_should_be_possible_to_update_product(self):
        productController = ProductController()
        product_name = product_mock["product_name"]
        model = product_mock["model"]
        category = product_mock["category"]
        quantity = product_mock["quantity"]
        sale_price = product_mock["sale_price"]
        purchase_price = product_mock["purchase_price"]
        product_id = productController.save_product(product_name, model, category, quantity, sale_price, purchase_price)
        old_product = productController.get_products(product_id)

        current_product_name = "updated"
        current_model = "updated"
        current_category = "updated"
        current_quantity = 89179312

        productController.update_product(product_id, current_product_name, current_model, current_category, current_quantity)
        current_product = productController.get_products(product_id)

        self.assertIsInstance(current_product, dict)
        self.assertIn("id", current_product)
        self.assertIn("model", current_product)
        self.assertIn("category", current_product)
        self.assertIn("quantity", current_product)
        self.assertIn("sale_price", current_product)
        self.assertIn("purchase_price", current_product)
        self.assertEqual(old_product["id"], current_product["id"])
        self.assertNotEqual(old_product["product_name"], current_product["product_name"])
        self.assertNotEqual(old_product["quantity"], current_product["quantity"])
        self.assertNotEqual(old_product["category"], current_product["category"])
        self.assertNotEqual(old_product["model"], current_product["model"])

    def test_it_should_not_be_possible_to_update_product_with_invalid_id(self):
        productController = ProductController()
        invalid_product_id = "ERROR"

        with self.assertRaises(Exception):
            productController.update_product(invalid_product_id)

class ProductControllerDeleteProduct(TestCase):

    def test_it_should_be_possible_to_delete_product(self):
        productController = ProductController()
        product_name = product_mock["product_name"]
        model = product_mock["model"]
        category = product_mock["category"]
        quantity = product_mock["quantity"]
        sale_price = product_mock["sale_price"]
        purchase_price = product_mock["purchase_price"]
        product_id = productController.save_product(product_name, model, category, quantity, sale_price, purchase_price)


        productController.delete_product(product_id)

        with self.assertRaises(NotFoundException):
            productController.get_products(product_id)

    def test_it_should_not_be_possible_to_delete_product_with_invalid_id(self):
        productController = ProductController()
        invalid_product_id = "ERROR"

        with self.assertRaises(NotFoundException):
            productController.delete_product(invalid_product_id)