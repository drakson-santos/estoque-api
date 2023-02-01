import uuid
from repositories import IRepository
from databases import IDatabase
from models import Model

class ModelRepositorySqlLite(IRepository):

    def __init__(self, database):
        self.database: IDatabase = database
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        sql = f"CREATE TABLE models (id TEXT PRIMARY KEY,  name TEXT)"
        self.database.create_table_if_not_exists("models", sql)

    def create(self, name):
        sql = 'INSERT INTO models (id, name) VALUES (?, ?)'
        model_id = str(uuid.uuid4())
        model_id = self.database.create(sql, (model_id, name))
        return Model(model_id, name)

    def read(self, model_id=None):
        if model_id:
            return self.get_by_id(model_id)
        return self.get_all()

    def get_all(self):
        sql = 'SELECT * FROM models'
        rows = self.database.read(sql)
        models = []
        for row in rows:
            model = Model(row[0], row[1])
            models.append(model)
        return models

    def get_by_id(self, model_id):
        sql = 'SELECT * FROM models WHERE id = ?'
        row = self.database.read(sql, (model_id,))[0]
        if row:
            return Model(row[0], row[1])
        return None

    def delete(self, model_id):
        sql = 'DELETE FROM models WHERE id = ?'
        self.database.delete(sql, (model_id,))

    def update(self, model_id, name=None):
        """
        Update model in the repository
        """
        update_query = "UPDATE models SET"
        update_values = []
        if name:
            update_query += " name = ?,"
            update_values.append(name)

        # remove last comma
        update_query = update_query[:-1]
        update_query += " WHERE id = ?"
        update_values.append(model_id)

        self.database.update(update_query, tuple(update_values))

        return self.get_by_id(model_id)