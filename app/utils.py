import json
import os

from app import app


def read_json(path):
    with open(path, "r") as f:
        return json.load(f)

def load_categories():
    return read_json(os.path.join(app.root_path, 'static/data/categories.json'))

def load_products():
    return read_json(os.path.join(app.root_path, 'static/data/products.json'))

def format_price(amount, currency="$"):
    return "{1}{0:,.1f}".format(amount, currency)