# from flask import request, Blueprint
# from controllers.model.ModelController import ModelController
# from repository.inMemoryRepository.inMemory import InMemoryRepository
# from exceptions.api.NotFoundException import NotFoundException

# bp_models = Blueprint("models", __name__)

# @bp_models.route('/models', methods=["GET"])
# def get_model():
#     model_id =  request.args.get("model_id")
#     try:
#         model = ModelController(InMemoryRepository()).get_model(model_id)
#     except NotFoundException as error:
#         return {
#             "message": error.message,
#         }, error.http_code

#     return {
#         "models": model
#     }

# @bp_models.route('/models', methods=["POST"])
# def save_model():
#     model_name = request.json["model_name"]

#     try:
#         ModelController(InMemoryRepository()).save_model(model_name)
#     except Exception as error:
#         return{
#             "message": str(error.message),
#         }, 500

#     return {
#         "id": model_name
#     }, 201
# @bp_models.route('/models', methods=["PUT"])
# def update_model():
#     model_id = request.args.get("model_id")
#     model_name = request.json.get("model_name")

#     try:
#         ModelController(InMemoryRepository()).update_model(model_id, model_name)
#     except NotFoundException as error:
#         return{
#             "message": error.message,
#         },error.http_code

#     return {
#         "id": model_id
#     },200

# @bp_models.route('/models', methods=["DELETE"])
# def delete_model():
#     model_id = request.args.get("model_id")

#     try:
#         ModelController(InMemoryRepository()).delete_model(model_id)
#     except NotFoundException as error:
#         return {
#             "message": error.message
#         }, error.http_code

#     return {}, 204