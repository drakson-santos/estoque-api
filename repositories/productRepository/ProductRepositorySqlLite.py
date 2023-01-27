import uuid
from repositories import IRepository
from databases import IDatabase
from models import Product
class ProductRepositorySqlLite(IRepository):

    def __init__(self, database):
        self.database: IDatabase = database
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        sql = f"CREATE TABLE products (id TEXT PRIMARY KEY,  name TEXT, model TEXT, category TEXT, quantity INTEGER, sale_price FLOAT, purchase_price FLOAT, photo TEXT)"
        self.database.create_table_if_not_exists("products", sql)

    def create(self, name, model, category, quantity, sale_price, purchase_price, photo):
        sql = 'INSERT INTO products (id, name, model, category, quantity, sale_price, purchase_price, photo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        product_id = str(uuid.uuid4())
        product_id = self.database.create(sql, (
            product_id,
            name,
            model,
            category,
            quantity,
            sale_price,
            purchase_price,
            photo
        ))
        return Product(
            product_id,
            name,
            model,
            category,
            quantity,
            sale_price,
            purchase_price,
            photo
        )

    def get_all(self):
        sql = 'SELECT * FROM products'
        rows = self.database.query(sql)
        products = []
        for row in rows:
            products.append(Product(*row))
        return products

    def get_by_id(self, product_id):
        sql = 'SELECT * FROM products WHERE id = ?'
        row = self.database.query(sql, (product_id,)).fetchone()
        if row:
            return Product(*row)
        return None

    def update(self, product):
        sql = 'UPDATE products SET name = ?, model = ?, category = ?, quantity = ?, sale_price = ?, purchase_price = ?, photo = ? WHERE id = ?'
        self.database.update(sql, (
            product.product_name,
            product.product_model,
            product.product_category,
            product.product_quantity,
            product.product_sale_price,
            product.product_purchase_price,
            product.product_photo,
            product.id
        ))

    def delete(self, product_id):
        sql = 'DELETE FROM products WHERE id = ?'
        self.database.delete(sql, (product_id,))

    def update(self, product_id, name=None, model=None, category=None, quantity=None, sale_price=None, purchase_price=None, photo=None):
        """
        Update product in the repository
        """
        update_query = "UPDATE products SET"
        update_values = []
        if name:
            update_query += " name = ?,"
            update_values.append(name)
        if model:
            update_query += " model = ?,"
            update_values.append(model)
        if category:
            update_query += " category = ?,"
            update_values.append(category)
        if quantity:
            update_query += " quantity = ?,"
            update_values.append(quantity)
        if sale_price:
            update_query += " sale_price = ?,"
            update_values.append(sale_price)
        if purchase_price:
            update_query += " purchase_price = ?,"
            update_values.append(purchase_price)
        if photo:
            update_query += " photo = ?,"
        update_values.append(photo)

        # remove last comma
        update_query = update_query[:-1]
        update_query += " WHERE id = ?"
        update_values.append(product_id)

        self.database.update(update_query, tuple(update_values))

        return self.get_by_id(product_id)