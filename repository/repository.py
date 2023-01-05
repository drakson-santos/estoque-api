from repository.baseRepository import BaseRepository
from repository.inMemoryRepository.inMemory import InMemoryRepository


class Repository(BaseRepository):

    def __init__(self):
        self.repository = InMemoryRepository()

    def get(self, table, id=None):
        return self.repository.get(table, id)

    def save(self, table, data):
        return self.repository.save(table, data)

    def update(self, table, id, data):
        return self.repository.update(table, id, data)

    def delete(self, table, id):
        return self.repository.delete(table, id)