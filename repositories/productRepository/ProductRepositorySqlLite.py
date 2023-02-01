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

    def read(self, product_id=None):
        if product_id:
            return self.get_by_id(product_id)
        return self.get_all()

    def get_all(self):
        sql = 'SELECT * FROM products'
        rows = self.database.read(sql)
        products = []
        for row in rows:
            product = Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            products.append(product)
        return products

    def get_by_id(self, product_id):
        sql = 'SELECT * FROM products WHERE id = ?'
        row = self.database.read(sql, (product_id,))[0]
        if row:
            product = Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            return product
        return None

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