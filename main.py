from flask import Flask
from flask import request
from controllers.ProductController import ProductController

app = Flask(__name__)

@app.route('/products', methods=["GET"])
def get_products():
    product_id =  request.args.get("product_id")
    products = ProductController().get_products(product_id)
    return {
        "products": products
    }


@app.route('/products', methods=["POST"])
def save_product():
    product_name = request.json["product_name"]
    model = request.json["model"]
    category = request.json["category"]
    quantity = request.json["quantity"]

    ProductController().save_product(
        product_name,
        model,
        category,
        quantity
    )

    return {
        "id": product_name
    }


@app.route('/products', methods=["PUT"])
def update_product():
    product_id =  request.args.get("product_id")
    product_name = request.json.get("product_name")
    model = request.json.get("model")
    category = request.json.get("category")
    quantity = request.json.get("quantity")

    ProductController().update_product(
        product_id,
        product_name,
        model,
        category,
        quantity
    )
    return "updated"

@app.route('/products', methods=["DELETE"])
def delete_product():
    product_id =  request.args.get("product_id")
    ProductController().delete_product(product_id)
    return "deleted"


if __name__ == '__main__':
    app.run(debug=True)
