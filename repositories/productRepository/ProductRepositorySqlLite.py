import uuid
from repositories import IRepository
from databases import IDatabase

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
        # return Product(product_id, product_name)
        return product_id