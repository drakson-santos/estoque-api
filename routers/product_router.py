from flask import jsonify, request, Blueprint

from databases.sql_lite import SqlLiteDatabase
from repositories.productRepository import ProductRepositorySqlLite
from controllers.product.ProductController import ProductController

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

@bp_products.route("/product/int:id", methods=["GET"])
def get_product(id):
    data_base = SqlLiteDatabase()
    product_repository = ProductRepositorySqlLite(data_base)
    product_controller = ProductController(product_repository)
    product = product_controller.get_product(id)
    return jsonify({"product": product.to_json()})

@bp_products.route("/product/int:id", methods=["PUT"])
def update_product(id):
    data_base = SqlLiteDatabase()
    product_repository = ProductRepositorySqlLite(data_base)
    product_controller = ProductController(product_repository)
    product_name = request.json.get("name")
    product = product_controller.update_product(id, product_name)
    return jsonify({"product": product.to_json()})

@bp_products.route("/product/int:id", methods=["DELETE"])
def delete_product(id):
    data_base = SqlLiteDatabase()
    product_repository = ProductRepositorySqlLite(data_base)
    product_controller = ProductController(product_repository)
    product_controller.delete_product(id)
    return jsonify({"message": "Product deleted successfully."})

@bp_products.route("/products", methods=["GET"])
def get_all_products():
    data_base = SqlLiteDatabase()
    product_repository = ProductRepositorySqlLite(data_base)
    product_controller = ProductController(product_repository)
    products = product_controller.get_all_products()
    return jsonify({"products": [product.to_json() for product in products]})