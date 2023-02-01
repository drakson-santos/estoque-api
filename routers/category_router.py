from flask import jsonify, request, Blueprint

from controllers.category.CategoryController import CategoryController
from repositories.productRepository import ProductRepositorySqlLite

bp_categories = Blueprint("categories", __name__)

category_controller = CategoryController(ProductRepositorySqlLite())

@bp_categories.route("/category", methods=["POST"])
def create_category():
    name = request.json.get("name")
    category = category_controller.create_category(name)
    return jsonify({"category": category})

@bp_categories.route("/category/int:id", methods=["GET"])
def get_category(id):
    category = category_controller.get_category(id)
    return jsonify({"category": category})

@bp_categories.route("/category/int:id", methods=["PUT"])
def update_category(id):
    category_name = request.json.get("name")
    category = category_controller.update_category(id, category_name)
    return jsonify({"category": category})

@bp_categories.route("/category/int:id", methods=["DELETE"])
def delete_category(id):
    category_controller.delete_category(id)
    return jsonify({"message": "Category deleted successfully."})

@bp_categories.route("/categories", methods=["GET"])
def get_all_categories():
    categories = category_controller.get_all_categories()
    return jsonify({"categories": categories})