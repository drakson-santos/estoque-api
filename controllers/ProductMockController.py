# from controllers.category.CategoryController import CategoryController
# from controllers.model.ModelController import ModelController
# from controllers.product.ProductController import ProductController
# from repository.inMemoryRepository.inMemory import InMemoryRepository
# class ProductMockController:

#     def save_mock(self):
#         categoryController = CategoryController(InMemoryRepository())
#         modelController = ModelController(InMemoryRepository())
#         productController = ProductController(InMemoryRepository())

#         category_id = categoryController.save_category("category 1")
#         model_id = modelController.save_model("model 1")
#         productController.save_product("product 1", model_id, category_id, 12, 45, 20)