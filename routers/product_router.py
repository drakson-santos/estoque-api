from flask import request, Blueprint

from controllers.product.ProductController import ProductController
from controllers.category.CategoryController import CategoryController
from controllers.model.ModelController import ModelController
from repository.inMemoryRepository.inMemory import InMemoryRepository
from exceptions.api.NotFoundException import NotFoundException

bp_product = Blueprint("product", __name__)

@bp_product.route('/products', methods=["GET"])
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


@bp_product.route('/products', methods=["POST"])
def save_product():
    product_name = request.form["product_name"]
    model = request.form["model"]
    category = request.form["category"]
    quantity = request.form["quantity"]
    sale_price = request.form.get("sale_price")
    purchase_price = request.form.get("purchase_price")
    photo = request.files.get("photo")

    try:
        product_id = ProductController(InMemoryRepository()).save_product(
            product_name,
            model,
            category,
            quantity,
            sale_price,
            purchase_price,
            photo,
        )

    except Exception as error:
        return {
            "message": str(error),
        }, 500

    return {
        "id": product_id
    }, 201


@bp_product.route('/products', methods=["PUT"])
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

@bp_product.route('/products', methods=["DELETE"])
def delete_product():
    product_id =  request.args.get("product_id")

    try:
        ProductController(InMemoryRepository()).delete_product(product_id)
    except NotFoundException as error:
        return {
            "message": error.message,
        }, error.http_code

    return {}, 204