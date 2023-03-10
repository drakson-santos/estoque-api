from flask import jsonify, request, Blueprint

from databases.sql_lite import SqlLiteDatabase
from repositories.modelRepository import ModelRepositorySqlLite
from controllers.model.ModelController import ModelController

bp_models = Blueprint("models", __name__)


@bp_models.route("/model", methods=["POST"])
def create_model():
    data_base = SqlLiteDatabase()
    model_repository = ModelRepositorySqlLite(data_base)
    model_controller = ModelController(model_repository)

    name = request.json.get("name")
    model = model_controller.create_model(name)
    return jsonify({"model": model.to_json()})

@bp_models.route("/models", methods=["GET"])
def get_all_models():
    data_base = SqlLiteDatabase()
    model_repository = ModelRepositorySqlLite(data_base)
    model_controller = ModelController(model_repository)

    models = model_controller.get_all_models()
    return jsonify({"models": [model.to_json() for model in models] })

@bp_models.route("/model", methods=["GET"])
def get_model():
    data_base = SqlLiteDatabase()
    model_repository = ModelRepositorySqlLite(data_base)
    model_controller = ModelController(model_repository)

    id = request.args.get("id")
    model = model_controller.get_model(id)
    return jsonify({"model": model.to_json()})

@bp_models.route("/model", methods=["PUT"])
def update_model():
    data_base = SqlLiteDatabase()
    model_repository = ModelRepositorySqlLite(data_base)
    model_controller = ModelController(model_repository)

    id = request.args.get("id")
    model_name = request.json.get("name")
    model = model_controller.update_model(id, model_name)
    return jsonify({"model": model.to_json()})

@bp_models.route("/model", methods=["DELETE"])
def delete_model():
    data_base = SqlLiteDatabase()
    model_repository = ModelRepositorySqlLite(data_base)
    model_controller = ModelController(model_repository)

    id = request.args.get("id")
    model_controller.delete_model(id)
    return jsonify({"message": "Model deleted successfully."})

