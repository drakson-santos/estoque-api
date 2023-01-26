from abc import ABC, abstractmethod

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