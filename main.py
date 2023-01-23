from flask import Flask
from flask import request
from flask_cors import CORS

from controllers.product.ProductController import ProductController
from controllers.category.CategoryController import CategoryController
from controllers.model.ModelController import ModelController
from controllers.ProductMockController import ProductMockController
from exceptions.api.NotFoundException import NotFoundException

from repository.inMemoryRepository.inMemory import InMemoryRepository

app = Flask(__name__)

@app.route('/products', methods=["GET"])
def get_products():
    product_id =  request.args.get("product_id")

    try:
        products = ProductController(InMemoryRepository()).get_products(product_id)

        modelController = ModelController(InMemoryRepository())
        categoryController = CategoryController(InMemoryRepository())

        if isinstance(products, list):
            for product in products:
                model_id = product.get("model")
                category_id = product.get("category")
                if isinstance(model_id, dict):
                    model_id = model_id.get("id")
                    category_id = category_id.get("id")

                product["model"] = modelController.get_model(model_id)
                product["category"] = categoryController.get_category(category_id)
        else:
            products["model"] = modelController.get_model(model_id=product["model"])
            products["category"] = categoryController.get_category(category_id=product["category"])

    except NotFoundException as error:
        return {
            "message": error.message,
        }, error.http_code

    return {
        "products": products
    }


@app.route('/products', methods=["POST"])
def save_product():
    product_name = request.form["product_name"]
    model = request.form["model"]
    category = request.form["category"]
    quantity = request.form["quantity"]
    photo = request.files.get("photo")
    sale_price = request.json.get("sale_price")
    purchase_price = request.json.get("purchase_price")

    try:
        product_id = ProductController(InMemoryRepository()).save_product(
            product_name,
            model,
            category,
            quantity,
            photo,
            sale_price,
            purchase_price
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
    sale_price = request.json.get("sale_price")
    purchase_price = request.json.get("purchase_price")

    try:
        product_id = ProductController(InMemoryRepository()).update_product(
            product_id,
            product_name,
            model,
            category,
            quantity,
            sale_price,
            purchase_price
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
        ProductController(InMemoryRepository()).delete_product(product_id)
    except NotFoundException as error:
        return {
            "message": error.message,
        }, error.http_code

    return {}, 204


@app.route('/categories', methods=["GET"])
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

@app.route('/categories', methods=["POST"])
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
@app.route('/categories', methods=["PUT"])
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

@app.route('/categories', methods=["DELETE"])
def delete_category():
    category_id = request.args.get("category_id")

    try:
        CategoryController(InMemoryRepository()).delete_category(category_id)
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
        model = ModelController(InMemoryRepository()).get_model(model_id)
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
        ModelController(InMemoryRepository()).save_model(model_name)
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
        ModelController(InMemoryRepository()).update_model(model_id, model_name)
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
        ModelController(InMemoryRepository()).delete_model(model_id)
    except NotFoundException as error:
        return {
            "message": error.message
        }, error.http_code

    return {}, 204



if __name__ == '__main__':
    ProductMockController().save_mock()
    CORS(app)
    app.run(debug=True)
