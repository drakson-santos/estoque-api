from flask import Flask
from flask import request
from flask_cors import CORS
from controllers.ProductController import ProductController
from controllers.CategoryController import CategoryController
from controllers.ModelController import ModelController
from controllers.ProductMockController import ProductMockController
from exceptions.api.NotFoundException import NotFoundException
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static"
app.config["SERVER_NAME"] = "localhost:5000"

@app.route('/products', methods=["GET"])
def get_products():
    product_id =  request.args.get("product_id")

    try:
        products = ProductController().get_products(product_id)
    except NotFoundException as error:
        return {
            "message": error.message,
        }, error.http_code

    return {
        "products": products
    }


@app.route('/products', methods=["POST"])
def save_product():
    # product_name = request.json["product_name"]
    # model = request.json["model"]
    # category = request.json["category"]
    # quantity = request.json["quantity"]
    product_name = request.form["product_name"]
    model = request.form["model"]
    category = request.form["category"]
    quantity = request.form["quantity"]
    photo = request.files.get("photo")

    if photo:
        file = request.files['photo']
        if file.filename != '':
            filename = secure_filename(file.filename)
            photo = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(photo)
            photo_url = "http://"+app.config["SERVER_NAME"]+"/"+app.config["UPLOAD_FOLDER"]+"/"+filename

    try:
        product_id = ProductController().save_product(
            product_name,
            model,
            category,
            quantity,
            photo_url
        )

    except Exception as error:
        return {
            "message": str(error.message),
        }, 500

    return {
        "id": product_id
    }, 201


@app.route('/products', methods=["PUT"])
def update_product():
    product_id =  request.args.get("product_id")
    product_name = request.json.get("product_name")
    model = request.json.get("model")
    category = request.json.get("category")
    quantity = request.json.get("quantity")

    try:
        product_id = ProductController().update_product(
            product_id,
            product_name,
            model,
            category,
            quantity
        )
    except NotFoundException as error:
        return {
            "message": error.message,
        }, error.http_code

    return {
        "id": product_id
    }, 200

@app.route('/products', methods=["DELETE"])
def delete_product():
    product_id =  request.args.get("product_id")

    try:
        ProductController().delete_product(product_id)
    except NotFoundException as error:
        return {
            "message": error.message,
        }, error.http_code

    return {}, 204


@app.route('/categories', methods=["GET"])
def get_categories():
    category_id =  request.args.get("category_id")
    try:
        category = CategoryController().get_category(category_id)
    except NotFoundException as error:
        return {
            "message": error.message,
        }, error.http_code

    return {
        "categories": category
    }

@app.route('/categories', methods=["POST"])
def save_category():
    category_name = request.json["category_name"]

    try:
        CategoryController().save_category(category_name)
    except Exception as error:
        return{
            "message": str(error.message),
        }, 500

    return {
        "id": category_name
    }, 201
@app.route('/categories', methods=["PUT"])
def update_category():
    category_id = request.args.get("category_id")
    category_name = request.json.get("category_name")

    try:
        CategoryController().update_category(category_id, category_name)
    except NotFoundException as error:
        return{
            "message": error.message,
        },error.http_code

    return {
        "id": category_id
    },200

@app.route('/categories', methods=["DELETE"])
def delete_category():
    category_id = request.args.get("category_id")

    try:
        CategoryController().delete_category(category_id)
    except NotFoundException as error:
        return {
            "message": error.message
        }, error.http_code

    return {}, 204

#######################################################################################

@app.route('/models', methods=["GET"])
def get_model():
    model_id =  request.args.get("model_id")
    try:
        model = ModelController().get_model(model_id)
    except NotFoundException as error:
        return {
            "message": error.message,
        }, error.http_code

    return {
        "models": model
    }

@app.route('/models', methods=["POST"])
def save_model():
    model_name = request.json["model_name"]

    try:
        ModelController().save_model(model_name)
    except Exception as error:
        return{
            "message": str(error.message),
        }, 500

    return {
        "id": model_name
    }, 201
@app.route('/models', methods=["PUT"])
def update_model():
    model_id = request.args.get("model_id")
    model_name = request.json.get("model_name")

    try:
        ModelController().update_model(model_id, model_name)
    except NotFoundException as error:
        return{
            "message": error.message,
        },error.http_code

    return {
        "id": model_id
    },200

@app.route('/models', methods=["DELETE"])
def delete_model():
    model_id = request.args.get("model_id")

    try:
        ModelController().delete_model(model_id)
    except NotFoundException as error:
        return {
            "message": error.message
        }, error.http_code

    return {}, 204



if __name__ == '__main__':
    ProductMockController().save_mock()
    CORS(app)
    app.run(debug=True)
