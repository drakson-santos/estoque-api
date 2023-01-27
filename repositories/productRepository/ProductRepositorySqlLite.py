import uuid
from repositories import IRepository
from databases import IDatabase
from models import Product
class ProductRepositorySqlLite(IRepository):

    def __init__(self, database):
        self.database: IDatabase = database
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        sql = f"CREATE TABLE products (id TEXT PRIMARY KEY,  product_model TEXT, product_category TEXT, product_quantity INTEGER, product_sale_price FLOAT, product_purchase_price FLOAT, product_photo TEXT)"
        self.database.create_table_if_not_exists("products", sql)

    def create(self,
        product_name,
        product_model,
        product_category,
        product_quantity,
        product_sale_price,
        product_purchase_price,
        product_photo
    ):
        sql = 'INSERT INTO products (id, product_name, product_model, product_category, product_quantity, product_sale_price, product_purchase_price, product_photo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        product_id = str(uuid.uuid4())
        product_id = self.database.create(sql, (
            product_id,
            product_name,
            product_model,
            product_category,
            product_quantity,
            product_sale_price,
            product_purchase_price,
            product_photo
        ))
        return Product(
            product_id,
            product_name,
            product_model,
            product_category,
            product_quantity,
            product_sale_price,
            product_purchase_price,
            product_photo
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
        sql = 'UPDATE products SET product_name = ?, product_model = ?, product_category = ?, product_quantity = ?, product_sale_price = ?, product_purchase_price = ?, product_photo = ? WHERE id = ?'
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

    def update(self, product_id, product_name=None, product_model=None, product_category=None, product_quantity=None, product_sale_price=None, product_purchase_price=None, product_photo=None):
        """
        Update product in the repository
        """
        update_query = "UPDATE products SET"
        update_values = []
        if product_name:
            update_query += " product_name = ?,"
            update_values.append(product_name)
        if product_model:
            update_query += " product_model = ?,"
            update_values.append(product_model)
        if product_category:
            update_query += " product_category = ?,"
            update_values.append(product_category)
        if product_quantity:
            update_query += " product_quantity = ?,"
            update_values.append(product_quantity)
        if product_sale_price:
            update_query += " product_sale_price = ?,"
            update_values.append(product_sale_price)
        if product_purchase_price:
            update_query += " product_purchase_price = ?,"
            update_values.append(product_purchase_price)
        if product_photo:
            update_query += " product_photo = ?,"
        update_values.append(product_photo)

        # remove last comma
        update_query = update_query[:-1]
        update_query += " WHERE id = ?"
        update_values.append(product_id)

        self.database.update(update_query, tuple(update_values))

        return self.get_by_id(product_id)