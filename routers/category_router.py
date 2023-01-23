from flask import request, Blueprint

from controllers.category.CategoryController import CategoryController
from repository.inMemoryRepository.inMemory import InMemoryRepository
from exceptions.api.NotFoundException import NotFoundException

bp_categories = Blueprint("categories", __name__)

@bp_categories.route('/categories', methods=["GET"])
def get_categories():
    category_id =  request.args.get("category_id")
    try:
        category = CategoryController(InMemoryRepository()).get_category(category_id)
    except NotFoundException as error:
        return {
            "message": error.message,
        }, error.http_code

    return {
        "categories": category
    }

@bp_categories.route('/categories', methods=["POST"])
def save_category():
    category_name = request.json["category_name"]

    try:
        CategoryController(InMemoryRepository()).save_category(category_name)
    except Exception as error:
        return{
            "message": str(error.message),
        }, 500

    return {
        "id": category_name
    }, 201
@bp_categories.route('/categories', methods=["PUT"])
def update_category():
    category_id = request.args.get("category_id")
    category_name = request.json.get("category_name")

    try:
        CategoryController(InMemoryRepository()).update_category(category_id, category_name)
    except NotFoundException as error:
        return{
            "message": error.message,
        },error.http_code

    return {
        "id": category_id
    },200

@bp_categories.route('/categories', methods=["DELETE"])
def delete_category():
    category_id = request.args.get("category_id")

    try:
        CategoryController(InMemoryRepository()).delete_category(category_id)
    except NotFoundException as error:
        return {
            "message": error.message
        }, error.http_code

    return {}, 204
