from controllers.CategoryController import CategoryController
from controllers.ModelController import ModelController
from controllers.ProductController import ProductController

class ProductMockController:

    def save_mock(self):
        categoryController = CategoryController()
        modelController = ModelController()
        productController = ProductController()

        categoryController.save_category("category 1")
        modelController.save_model("model 1")
        productController.save_product("product 1", "model 1", "category 1", 20)