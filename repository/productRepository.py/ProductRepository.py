from repository.baseRepository import IRepository
from databases.IDatabase import IDatabase
from databases.sql_lite.SqlLite import SqlLiteDatabase

class Product:

    def __init__(self,id, product_name):
        self.id = id
        self.product_name = product_name

class ProductRepositorySqlLite(IRepository):

    def __init__(self, database):
        self.database: IDatabase = database

    def create(self, product_name):
        sql = 'INSERT INTO products (product_name) VALUES (?)'
        product_id = self.database.create(sql, (product_name))
        return Product(product_id, product_name)


database = SqlLiteDatabase("products")
productRepository = ProductRepositorySqlLite(database)