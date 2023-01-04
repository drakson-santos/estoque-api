class BaseRepository:

    def get(self, id=None):
        raise NotImplementedError()

    def save(self, table, data):
        raise NotImplementedError()

    def update(self, table, id, data):
        raise NotImplementedError()

    def delete(self, table, id):
        raise NotImplementedError()


class InMemoryRepository(BaseRepository):
    _DATABASE = {}

    def get(self, table, id=None):
        data = list([])
        if self._DATABASE.get(table) is not None:
            data = self._DATABASE[table]

        if id:
            for element in data:
                if element["product_name"] == id:
                    return element
            return dict({})
        return data

    def save(self, table, data):
        if self._DATABASE.get(table) is None:
            self._DATABASE[table] = []
        self._DATABASE[table].append(data)

    def update(self, table, id, new_element):
        data = list([])
        if self._DATABASE.get(table) is not None:
            data = self._DATABASE[table]

        for index, element in enumerate(data):
            if element["product_name"] == id:
                data[index] = new_element

        self._DATABASE[table] = data


    def delete(self, table, id):
        data = list([])
        if self._DATABASE.get(table) is not None:
            data = self._DATABASE[table]

        new_data = list([])
        for element in data:
            if element["product_name"] != id:
                new_data.append(element)

        self._DATABASE[table] = new_data

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