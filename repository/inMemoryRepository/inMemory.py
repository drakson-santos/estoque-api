from ..baseRepository import BaseRepository

class InMemoryRepository(BaseRepository):
    _DATABASE = {}

    def get(self, table, id=None):
        data = list([])
        if self._DATABASE.get(table) is not None:
            data = self._DATABASE[table]

        if id:
            for element in data:
                if element["id"] == id:
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
            if element["id"] == id:
                data[index] = new_element

        self._DATABASE[table] = data


    def delete(self, table, id):
        data = list([])
        if self._DATABASE.get(table) is not None:
            data = self._DATABASE[table]

        new_data = list([])
        for element in data:
            if element["id"] != id:
                new_data.append(element)

        self._DATABASE[table] = new_data
