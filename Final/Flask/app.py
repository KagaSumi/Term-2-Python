import csv, os

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/store/<string:name>")
def get_store_products(name):
    """Gets the store's products
    Fix: Path was not going into the data folder had to add a path change
    """
    try:
        with open(f"./data/{name}.txt", "r") as fp: 
            reader = csv.reader(fp)
            data = [line for line in reader]
            return jsonify({"products": data})
    except FileNotFoundError:
        return "File Not Found",404

@app.route("/api/product/<string:name>", methods=["GET"])
def get_product(name):
    """Checks local fil for product name
    and returns where and how many we have of it
    """
    output = {
        "product": name,
        "available": 0,
        "stores" : {}
    }
    for file in os.listdir("./data"):
        with open(f"./data/{file}", "r") as fp:
            reader = csv.reader(fp)
            value = [line[1] for line in reader if line[0].lower() == name.lower()]
            if value:
                output["available"] += int(value[0])
                output["stores"][file[:-3]] = value[0]
    return jsonify(output)
            