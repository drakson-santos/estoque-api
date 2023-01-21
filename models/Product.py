class Product:

    def __init__(self,id, product_name, model, category, quantity, photo=None):
        self.id = id
        self.product_name = product_name
        self.model = model
        self.category = category
        self.quantity = quantity
        self.photo = photo
