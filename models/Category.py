class Category:

    def __init__(self, id, category_name):
        self.id = id
        self.name = category_name

    def to_json(self):
        return {'id': self.id, 'name': self.name}