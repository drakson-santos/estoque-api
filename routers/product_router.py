from flask import jsonify, request, Blueprint

from databases.sql_lite import SqlLiteDatabase
from repositories.productRepository import ProductRepositorySqlLite
from controllers.product.ProductController import ProductController
from repositories.categoryRepository import CategoryRepositorySqlLite
from controllers.category.CategoryController import CategoryController
from repositories.modelRepository import ModelRepositorySqlLite
from controllers.model.ModelController import ModelController

bp_products = Blueprint("products", __name__)

@bp_products.route("/product", methods=["POST"])
def create_product():
    data_base = SqlLiteDatabase()
    product_repository = ProductRepositorySqlLite(data_base)
    product_controller = ProductController(product_repository)

    name = request.json.get("name")
    model = request.json.get("model")
    category = request.json.get("category")
    quantity = request.json.get("quantity")
    sale_price = request.json.get("sale_price")
    purchase_price = request.json.get("purchase_price")
    photo = request.json.get("photo")

    product = product_controller.create_product(
        name, model, category, quantity, sale_price, purchase_price, photo)
    return jsonify({"product": product.to_json()})

@bp_products.route("/products", methods=["GET"])
def get_all_products():
    data_base = SqlLiteDatabase()
    product_repository = ProductRepositorySqlLite(data_base)
    product_controller = ProductController(product_repository)

    model_repository = ModelRepositorySqlLite(data_base)
    model_controller = ModelController(model_repository)

    category_repository = CategoryRepositorySqlLite(data_base)
    category_controller = CategoryController(category_repository)

    response = []

    products = product_controller.get_all_products()
    if products:
        for product in products:
            product = product.to_json()
            
            product_model = model_controller.get_model(product["model"]) 
            product_category = category_controller.get_category(product["category"])
            
            product["model"] = product_model.to_json()
            product["category"] = product_category.to_json()
            
            response.append(product)

    return jsonify({"products": response })

@bp_products.route("/product", methods=["GET"])
def get_product():
    data_base = SqlLiteDatabase()
    product_repository = ProductRepositorySqlLite(data_base)
    product_controller = ProductController(product_repository)

    id = request.args.get("id")
    product = product_controller.get_product(id)

    return jsonify({"product": product.to_json()})

@bp_products.route("/product", methods=["PUT"])
def update_product():
    data_base = SqlLiteDatabase()
    product_repository = ProductRepositorySqlLite(data_base)
    product_controller = ProductController(product_repository)

    name = request.json.get("name")
    model = request.json.get("model")
    category = request.json.get("category")
    quantity = request.json.get("quantity")
    sale_price = request.json.get("sale_price")
    purchase_price = request.json.get("purchase_price")
    photo = request.json.get("photo")

    id = request.args.get("id")
    product = product_controller.update_product(id,
        name, model, category, quantity, sale_price, purchase_price, photo)
    return jsonify({"product": product.to_json()})

@bp_products.route("/product", methods=["DELETE"])
def delete_product():
    data_base = SqlLiteDatabase()
    product_repository = ProductRepositorySqlLite(data_base)
    product_controller = ProductController(product_repository)

    id = request.args.get("id")
    product_controller.delete_product(id)
    return jsonify({"message": "Product deleted successfully."})

