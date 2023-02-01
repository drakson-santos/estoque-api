class Product:

    def __init__(self,id, name, model, category, quantity, sale_price, purchase_price, photo=None):
        self.id = id
        self.name = name
        self.model = model
        self.category = category
        self.quantity = quantity
        self.sale_price = sale_price
        self.purchase_price = purchase_price
        self.photo = photo

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'category': self.category,
            'quantity': self.quantity,
            'sale_price': self.sale_price,
            'purchase_price': self.purchase_price,
            'photo': self.photo
        }
