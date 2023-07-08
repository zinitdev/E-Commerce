import json
import os

from app import app
from app.models import *

def read_json(path):
    with open(path, "r") as f:
        return json.load(f)

def load_categories():
    return Category.query.all()

def load_products(cate_id=None, kw=None, from_price=None, to_price=None):
    products = Product.query.filter(Product.active.__eq__(True)).all()
    
    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))
        
    if kw:
        products = products.filter(Product.name.contains(kw))    
    
    if from_price:
        products = products.filter(Product.price.__ge__(from_price))
    
    if to_price:
        products = products.filter(Product.price.__le__(to_price))
    
    return products

def format_price(amount, currency="$"):
    return "{1}{0:,.1f}".format(amount, currency)

def get_product_by_id(product_id):
    return Product.query.get(product_id)