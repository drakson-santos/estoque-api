from flask import jsonify, request, Blueprint

from databases.sql_lite import SqlLiteDatabase
from repositories.categoryRepository import CategoryRepositorySqlLite
from controllers.category.CategoryController import CategoryController

bp_categories = Blueprint("categories", __name__)


@bp_categories.route("/category", methods=["POST"])
def create_category():
    data_base = SqlLiteDatabase()
    category_repository = CategoryRepositorySqlLite(data_base)
    category_controller = CategoryController(category_repository)

    name = request.json.get("name")
    category = category_controller.create_category(name)
    return jsonify({"category": category.to_json()})

@bp_categories.route("/categories", methods=["GET"])
def get_all_categories():
    data_base = SqlLiteDatabase()
    category_repository = CategoryRepositorySqlLite(data_base)
    category_controller = CategoryController(category_repository)

    categories = category_controller.get_all_categories()
    return jsonify({"categories": [category.to_json() for category in categories] })

@bp_categories.route("/category", methods=["GET"])
def get_category():
    data_base = SqlLiteDatabase()
    category_repository = CategoryRepositorySqlLite(data_base)
    category_controller = CategoryController(category_repository)

    id = request.args.get("id")
    category = category_controller.get_category(id)
    return jsonify({"category": category.to_json()})

@bp_categories.route("/category", methods=["PUT"])
def update_category():
    data_base = SqlLiteDatabase()
    category_repository = CategoryRepositorySqlLite(data_base)
    category_controller = CategoryController(category_repository)

    id = request.args.get("id")
    category_name = request.json.get("name")
    category = category_controller.update_category(id, category_name)
    return jsonify({"category": category.to_json()})

@bp_categories.route("/category", methods=["DELETE"])
def delete_category():
    data_base = SqlLiteDatabase()
    category_repository = CategoryRepositorySqlLite(data_base)
    category_controller = CategoryController(category_repository)

    id = request.args.get("id")
    category_controller.delete_category(id)
    return jsonify({"message": "Category deleted successfully."})

