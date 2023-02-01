from flask import jsonify, request, Blueprint

from databases.sql_lite import SqlLiteDatabase
from repositories.modelRepository import ModelRepositorySqlLite
from controllers.model.ModelController import ModelController

bp_models = Blueprint("categories", __name__)


@bp_models.route("/model", methods=["POST"])
def create_model():
    data_base = SqlLiteDatabase()
    model_repository = ModelRepositorySqlLite(data_base)
    model_controller = ModelController(model_repository)

    name = request.json.get("name")
    model = model_controller.create_model(name)
    return jsonify({"model": model.to_json()})

@bp_models.route("/model/int:id", methods=["GET"])
def get_model(id):
    data_base = SqlLiteDatabase()
    model_repository = ModelRepositorySqlLite(data_base)
    model_controller = ModelController(model_repository)

    model = model_controller.get_model(id)
    return jsonify({"model": model.to_json()})

@bp_models.route("/model/int:id", methods=["PUT"])
def update_model(id):
    data_base = SqlLiteDatabase()
    model_repository = ModelRepositorySqlLite(data_base)
    model_controller = ModelController(model_repository)

    model_name = request.json.get("name")
    model = model_controller.update_model(id, model_name)
    return jsonify({"model": model.to_json()})

@bp_models.route("/model/int:id", methods=["DELETE"])
def delete_model(id):
    data_base = SqlLiteDatabase()
    model_repository = ModelRepositorySqlLite(data_base)
    model_controller = ModelController(model_repository)

    model_controller.delete_model(id)
    return jsonify({"message": "Model deleted successfully."})

@bp_models.route("/categories", methods=["GET"])
def get_all_categories():
    data_base = SqlLiteDatabase()
    model_repository = ModelRepositorySqlLite(data_base)
    model_controller = ModelController(model_repository)

    categories = model_controller.get_all_categories()
    return jsonify({"categories": [model.to_json() for model in categories] })