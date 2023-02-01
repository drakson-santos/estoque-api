import uuid
from repositories import IRepository
from databases import IDatabase
from models import Category

class CategoryRepositorySqlLite(IRepository):

    def __init__(self, database):
        self.database: IDatabase = database
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        sql = f"CREATE TABLE categories (id TEXT PRIMARY KEY,  name TEXT)"
        self.database.create_table_if_not_exists("categories", sql)

    def create(self, name):
        sql = 'INSERT INTO categories (id, name) VALUES (?, ?)'
        category_id = str(uuid.uuid4())
        category_id = self.database.create(sql, (category_id, name))
        return Category(category_id, name)

    def read(self, category_id=None):
        if category_id:
            return self.get_by_id(category_id)
        return self.get_all()

    def get_all(self):
        sql = 'SELECT * FROM categories'
        rows = self.database.read(sql)
        categories = []
        for row in rows:
            categories.append(row)
        return categories

    def get_by_id(self, category_id):
        sql = 'SELECT * FROM categories WHERE id = ?'
        row = self.database.read(sql, (category_id,))[0]
        if row:
            return row
        return None

    def delete(self, category_id):
        sql = 'DELETE FROM categories WHERE id = ?'
        self.database.delete(sql, (category_id,))

    def update(self, category_id, name=None):
        """
        Update category in the repository
        """
        update_query = "UPDATE categories SET"
        update_values = []
        if name:
            update_query += " name = ?,"
            update_values.append(name)

        # remove last comma
        update_query = update_query[:-1]
        update_query += " WHERE id = ?"
        update_values.append(category_id)

        self.database.update(update_query, tuple(update_values))

        return self.get_by_id(category_id)