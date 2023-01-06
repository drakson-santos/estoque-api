from flask import Flask
from flask import request
from controllers.ProductController import ProductController
from controllers.CategoryController import CategoryController
from exceptions.api.NotFoundException import NotFoundException

app = Flask(__name__)

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
    product_name = request.json["product_name"]
    model = request.json["model"]
    category = request.json["category"]
    quantity = request.json["quantity"]

    try:
        product_id = ProductController().save_product(
            product_name,
            model,
            category,
            quantity
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
    category = CategoryController().get_category(category_id)
    return {
        "Categories": category
    }

@app.route('/categories', methods=["POST"])
def save_category():
    category_name = request.json["category_name"]

    CategoryController().save_category(
        category_name
    )

    return {
        "id": category_name
    }
@app.route('/categories', methods=["PUT"])
def update_category():
    category_id = request.args.get("category_id")
    category_name = request.json.get("category_name")
    CategoryController().update_category(category_id, category_name)
    return "updated"

@app.route('/categories', methods=["DELETE"])
def delete_category():
    category_id = request.args.get("category_id")
    CategoryController().delete_category(category_id)
    return "deleted"
if __name__ == '__main__':
    app.run(debug=True)
