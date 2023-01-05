class BaseRepository:

    def get(self, id=None):
        raise NotImplementedError()

    def save(self, table, data):
        raise NotImplementedError()

    def update(self, table, id, data):
        raise NotImplementedError()

    def delete(self, table, id):
        raise NotImplementedError()
        