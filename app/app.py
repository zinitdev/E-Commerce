from flask import render_template, request

from app import app, utils


@app.context_processor
def utility_processor():
    return dict(
            format_price = utils.format_price,
            categories = utils.load_categories(),
        )

@app.route('/')
def home():
    cate_id = request.args.get('cate_id')
    
    products = utils.load_products(cate_id=cate_id)
    return render_template('pages/index.html',
                           title="Home", products=products)

@app.route('/products')
def products():
    products = utils.load_products()
    
    return render_template('pages/products.html',
                           title="Collections",
                           products=products)