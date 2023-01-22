from controllers.CategoryController import CategoryController
from controllers.model.ModelController import ModelController
from controllers.product.ProductController import ProductController
import os
class ProductMockController:

    def save_mock(self):
        categoryController = CategoryController()
        modelController = ModelController()
        productController = ProductController()

        category_id = categoryController.save_category("category 1")
        model_id = modelController.save_model("model 1")
        productController.save_product("product 1", model_id, category_id, 20)