from flask import render_template

from app import app, utils


@app.context_processor
def utility_processor():
    return dict(
            format_price = utils.format_price,
        )

@app.route('/')
def home():
    categories = utils.load_categories()
    
    return render_template('index.html', categories=categories)

@app.route('/products')
def products():
    products = utils.load_products()
    
    return render_template('products.html', products=products)