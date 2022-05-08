from sqlite3 import Cursor
from flask import Flask, request
import json
from mock_data import mock_catalog
from config import db

app = Flask("server")


@app.route("/")
def root():
    return "Hi there!"

    ##################
    ##################
    ##################

@app.route("/api/about", methods=["POST"])
def root ():
        me = {
            "first": "Savannah",
            "last": "Germino"
        }

        return  json.dumps(me) # parse into json, then return

@app.route("/api/catalog")
def get_catalog():
    return json.dumps(mock_catalog)



@app.route("/api/catalog")
def get_catalog():
    cursor = db.products.find({}) # get all 
    all_products = []

    for prod in cursor:
        all_products.append(prod)


        return json.dumps(all_products) 


@app.route("/api/catalog", methods=["post"])
def save_product():
    product = request.get_json()
    db.products.insert_one(product)

    print("Product saved!")
    print(product)

    product["_id"] = str(product["_id"])

    return json.dumps(product)

@app.route("/api/catalog/cheapest")
def get_cheapest():
    solution = mock_catalog[0]
    for prod in mock_catalog:
        if prod["price"] < solution["price"]:
            solution = prod 

    solution["_id"] = str(solution["_id"])
    return json.dumps(solution)


@app.route("/api/catalog/total")
def get_total():
    total = 0
    for prod in mock_catalog:
        total += prod ["price"]

    return json.dumps(total)





@app.route("/api/products/<id>")
def find_product(id):
    for prod in mock_catalog:
        if id == prod["_id"]:
            return json.dumps(prod)






@app.route("/api/products/categories")
def get_categories():
    categories = []


    for prod in mock_catalog:
        cat = prod["category"]
        if cat not in categories:
            categories.append(cat)

    return json.dumps(categories)




@app.route("/api/products/category/<name>")
def get_by_category(cat_name):
    results = []

    for prod in mock_catalog:
        if prod["category"].lower() == cat_name.lower():
            results.append(prod)

    return json.dumps(results)




@app.route("/api/products/search/<text>")
def search_by_text(text):
    results = []


    for prod in mock_catalog:
        title = prod["title"].lower()
        if text.lower() in title:
            results.append(prod)

    return json.dumps(results)

app.run(debug=True)






