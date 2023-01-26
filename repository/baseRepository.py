from abc import ABC, abstractmethod
class BaseRepository:

    def get(self, id=None):
        raise NotImplementedError()

    def save(self, table, data):
        raise NotImplementedError()

    def update(self, table, id, data):
        raise NotImplementedError()

    def delete(self, table, id):
        raise NotImplementedError()


class IRepository(ABC):
    @abstractmethod
    def create(self, object):
        pass

    # @abstractmethod
    # def read(self, object_id):
    #     pass

    # @abstractmethod
    # def update(self, object):
    #     pass

    # @abstractmethod
    # def delete(self, object_id):
    #     pass