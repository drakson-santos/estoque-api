import unittest
from unittest.mock import MagicMock
from repositories.productRepository import ProductRepositorySqlLite
from databases import IDatabase
from mocks import product_mock
from models import Product

class TestProductRepositorySqlLite(unittest.TestCase):

    def setUp(self):
        self.database = MagicMock(spec=IDatabase)
        self.product_repository = ProductRepositorySqlLite(self.database)

    def test_create_table_if_not_exists(self):
        self.product_repository.create_table_if_not_exists()
        self.database.create_table_if_not_exists.assert_called_with("products", "CREATE TABLE products (id TEXT PRIMARY KEY,  name TEXT, model TEXT, category TEXT, quantity INTEGER, sale_price FLOAT, purchase_price FLOAT, photo TEXT)")

    def test_create(self):
        product_name = product_mock["product_name"]
        product_model = product_mock["model"]
        product_category = product_mock["category"]
        product_quantity = product_mock["quantity"]
        product_sale_price = product_mock["sale_price"]
        product_purchase_price = product_mock["purchase_price"]
        product_photo = product_mock["photo"]

        product = self.product_repository.create(
            product_name,
            product_model,
            product_category,
            product_quantity,
            product_sale_price,
            product_purchase_price,
            product_photo
        )
        self.database.create.assert_called_once()
        self.assertIsInstance(product, Product)
        self.assertEqual(product.name, product_name)
        self.assertEqual(product.model, product_model)
        self.assertEqual(product.category, product_category)
        self.assertEqual(product.quantity, product_quantity)
        self.assertEqual(product.sale_price, product_sale_price)
        self.assertEqual(product.purchase_price, product_purchase_price)
        self.assertEqual(product.photo, product_photo)

    def test_get_all(self):
        products = [Product("1", "name1", "model1", "category1", 10, 10.0, 20.0, "photo1.jpg"),
                    Product("2", "name2", "model2", "category2", 20, 20.0, 30.0, "photo2.jpg")]
        self.database.read.return_value = products
        result = self.product_repository.get_all()
        self.database.read.assert_called_once_with("SELECT * FROM products")
        self.assertListEqual(result, products)

    def test_get_by_id(self):
        product = Product("1", "name", "model", "category", 10, 10.0, 20.0, "photo.jpg")
        self.database.read.return_value = [product]
        result = self.product_repository.get_by_id("1")
        self.database.read.assert_called_once_with("SELECT * FROM products WHERE id = ?", ("1",))
        self.assertEqual(result, product)

    def test_update(self):
        product = Product("1", "name", "model", "category", 10, 10.0, 20.0, "photo.jpg")
        self.product_repository.update(product.id, name='new name', model='new model', category='new category', quantity=15, sale_price=12.5, purchase_price=20.0)
        self.database.update.assert_called_once_with("UPDATE products SET name = ?, model = ?, category = ?, quantity = ?, sale_price = ?, purchase_price = ? WHERE id = ?", ('new name', 'new model', 'new category', 15, 12.5, 20.0, product.id))

    def test_delete(self):
        self.product_repository.delete("1")
        self.database.delete.assert_called_once_with("DELETE FROM products WHERE id = ?", ("1",))

