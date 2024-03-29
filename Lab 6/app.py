from pathlib import Path

from flask import Flask, jsonify, render_template, request

from database import db
from models import Product, Order, ProductsOrder

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
app.instance_path = Path(".").resolve()
db.init_app(app)


@app.route("/")
def home():
    data = Product.query.all()
    return render_template("index.html", products=data)


@app.route("/api/product/<string:name>", methods=["GET"])
def api_get_product(name):
    """Returns the user the product that belongs to the specified name.

    Args:
        name (str): Name of the product of the database

    Returns:
        Response : A response of the outcome of the get operation
    """
    product = db.session.get(Product, name.lower())
    if not product:
        return ("Product not found", 404)
    product_json = product.to_dict()
    return jsonify(product_json)


@app.route("/api/product/<string:name>", methods=["DELETE"])
def api_delete_product(name):
    """Deletes a product from the database

    Args:
        name (str): Name of the product of the database

    Returns:
        Response : A response of the outcome of the delete operation
    """
    product = db.session.get(Product, name.lower())
    if not product:
        return jsonify({"message": "Product not found."}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted."}), 200


@app.route("/api/product/<string:name>", methods=["PUT"])
def api_update_product(name):
    """Updating a product's price and quantity."

    Args:
        name (str): The name of the product you are updating.

    Raises:
        ValueError: Raises if we try to update an existing product with a new price and quantity where they are negative

    Returns:
        str: A string where it shows the updated product
    """
    data = request.json
    for key in ("price", "quantity"):
        if key not in data:
            return f"The JSON provided is invalid (missing: {key})", 400
    try:
        price = float(data["price"])
        quantity = int(data["quantity"])
        # Make sure they are positive
        if price < 0 or quantity < 0:
            raise ValueError
    except ValueError:
        return (
            "Invalid values: price must be a positive float and quantity a positive integer",
            400,
        )
    product = db.session.get(Product, name.lower())
    if not product:
        return ("Product not found.", 404)
    product.price = price
    product.quantity = quantity
    db.session.commit()
    return f"Product updated., product: {product.to_dict()}"


@app.route("/api/product", methods=["POST"])
def api_create_product():
    """The method creates a new product in our database.
    It requires a JSON payload representing the product.

    Raises:
        ValueError: This error is raised when the product does not have a positive price and quantity.

    Returns:
        str: String Confirming the product is added or any errors.
    """
    data = request.json
    # Check all data is provided
    for key in ("name", "price", "quantity"):
        if key not in data:
            return f"The JSON provided is invalid (missing: {key})", 400

    try:
        price = float(data["price"])
        quantity = int(data["quantity"])
        # Make sure they are positive
        if price < 0 or quantity < 0:
            raise ValueError
    except ValueError:
        return (
            "Invalid values: price must be a positive float and quantity a positive integer",
            400,
        )
    product = Product(
        name=data["name"],
        price=price,
        quantity=quantity,
    )
    db.session.add(product)
    db.session.commit()
    return "Item added to the database"


@app.route("/api/order/<int:order_id>", methods=["GET"])
def api_get_order(order_id):
    """Returns a response of a order in the form of a JSON object

    Args:
        order_id (int): integer representing the order id

    Returns:
        Response : JSON object representing order requested 
    """
    order = db.session.get(Order, order_id)
    if not order:
        return ("Order not found", 404)
    order = order.to_dict()
    return jsonify(order)


@app.route('/api/order', methods=['POST'])
def api_create_order():
    """This method creates a new order in our database

    Raises:
        ValueError: Throws an ValueError if order contains products that don't exist
        ValueError: Throws an ValueError if the products quantity is not a positive integer

    Returns:
        str: confirming order creation  
    """
    data = request.json
    for key in ("name", "address", "products"):
        if key not in data:
            return f"The JSON provided is invalid (missing: {key})", 400
    try:
        for product in data["products"]:
            if not db.session.get(Product, product['name'].lower()):
                raise ValueError()
    except ValueError:
        return ("Invalid values: products don't exist", 400)
    new_order = Order(
        name=data["name"], address=data["address"], completed=False, products=[])
    for product in data["products"]:
        try:
            quantity = int(product["quantity"])
            # Make sure they are positive
            if quantity < 0:
                raise ValueError
        except ValueError:
            return (
                "Invalid values: quantity a positive integer",
                400,
            )
        new_product = ProductsOrder(
            product_name=product["name"].lower(), quantity=product["quantity"])
        new_order.products.append(new_product)
    db.session.add(new_order)
    db.session.commit()
    return "Item added to the database"


@app.route("/api/order/<int:order_id>", methods=["PUT"])
def api_process_order(order_id):
    """Processes the order, by changing the order product quantity to either order quantity which ever is lesser.
    Then subtract it from the store stock and change the completed boolean to true."

    Args:
        order_id (int): The order id to process

    Returns:
        Response: A Json object representing the completed order
    """
    data = request.json
    if ("process") not in data:
        return ("The JSON provided is invalid (missing: process)", 400)
    order = db.session.get(Order, order_id)
    if data["process"]:
        if order.completed:
            return jsonify(order.to_dict())

        # Run thru order and see if quantity is greater than product
        for product in order.products:
            store_product = db.session.get(Product, product.product_name)
            product.quantity = store_product.process(product.quantity)
        order.completed = True
        db.session.commit()
    return jsonify(order.to_dict())

@app.route("/api/order/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    """Updates an order with a new set of products.

    Args:
        order_id (int): order id to find

    Returns:
        Response: A Json object representing the new order.
    """    
    data = request.json
    order = db.session.get(Order, order_id)
    order.products = data["products"]
    db.session.commit()
    return jsonify(order.to_dict())

if __name__ == "__main__":
    app.run(debug=True)
