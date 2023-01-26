from flask import Flask
from routers.product_router import bp_product
from routers.model_router import bp_models
from routers.category_router import bp_categories
from controllers.ProductMockController import ProductMockController

def create_app():
    ProductMockController().save_mock()


    app = Flask(__name__)

    with app.app_context():
        app.register_blueprint(bp_product)
        app.register_blueprint(bp_models)
        app.register_blueprint(bp_categories)

        return app