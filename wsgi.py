from flask import Flask
from routers.product_router import bp_products
from routers.model_router import bp_models
from routers.category_router import bp_categories

def create_app():
    app = Flask(__name__, static_folder='../web-development/build', static_url_path='/')
    
    with app.app_context():
        app.register_blueprint(bp_categories)
        app.register_blueprint(bp_models)
        app.register_blueprint(bp_products)
        
        return app