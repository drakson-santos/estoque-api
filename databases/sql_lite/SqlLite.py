import sqlite3
from IDatabase import IDatabase

class SqlLiteDatabase(IDatabase):

    def __init__(self):
        self.conn = sqlite3.connect('databases.sqlite')
        self.cursor = self.conn.cursor()
    #     self.create_table_if_not_exists(database_name)

    # def create_table_if_not_exists(self, database_name):
    #     self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (database_name,))
    #     if self.cursor.fetchone() is None:
    #         self.cursor.execute(f"CREATE TABLE {database_name} (id INTEGER PRIMARY KEY, product_name TEXT)")
    #         self.conn.commit()

    def create(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.lastrowid

    def read(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.rowcount

    def delete(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.rowcount

database = SqlLiteDatabase("products")

# class Product:

#     def __init__(self,id, product_name):
#         self.id = id
#         self.product_name = product_name

# class Repository(ABC):
#     @abstractmethod
#     def create(self, object):
#         pass

#     # @abstractmethod
#     # def read(self, object_id):
#     #     pass

#     # @abstractmethod
#     # def update(self, object):
#     #     pass

#     # @abstractmethod
#     # def delete(self, object_id):
#     #     pass

# class ProductRepositorySqlLite(Repository):

#     def __init__(self, database):
#         self.database: Database = database

#     def create(self, product_name):
#         sql = 'INSERT INTO products (product_name) VALUES (?)'
#         product_id = self.database.create(sql, (product_name))
#         return Product(product_id, product_name)


# class ProductController:

#     def __init__(self, product_repository):
#         self.product_repository: Repository = product_repository

#     def create_product(self, product_name):
#         return self.product_repository.create(product_name)

#     def get_product(self, id):
#         return self.product_repository.read(id)

#     def update_product(self, id, product_name):
#         return self.product_repository.update(id, product_name)

#     def delete_product(self, id):
#         return self.product_repository.delete(id)

#     def get_all_products(self):
#         return self.product_repository.read()

# database = SqlLiteDatabase("products")
# productRepository = ProductRepositorySqlLite(database)
# productController = ProductController(productRepository)

# productController.create_product("product 1")