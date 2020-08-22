from flask import Flask, render_template, request, url_for, redirect, flash
import os
from forms import ProductForm, ProductSaleForm
from models import products, new_product


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def mainpage():
    return render_template("mainpage.html")


@app.route('/dashboard', methods=["GET", "POST"])
def add_product():
    ITEMS = products.all()
    product_form = ProductForm()
    if request.method == "POST":
        if request.form["btn"] == "Add Product":
            if product_form.validate_on_submit():
                product = new_product.create(product_form.data)
                ITEMS = products.add(product)

        if request.form["btn"] == "Export Products":
            products.export()
        if request.form["btn"] == "Load Products": 
            ITEMS = products.load()

    return render_template("add_product.html", product_form=product_form, product_list=ITEMS)

@app.route('/sell/<product_name>', methods=["GET", "POST"])
def sell_product(product_name):
    ITEMS = products.all()
    product_sale_form = ProductSaleForm()
    if request.method == "POST":
        if product_sale_form.validate_on_submit():
            if product_name in ITEMS:
                quantity = product_sale_form.data['sold_quantity']
                ITEMS = products.sell(product_name, quantity)
                return redirect(url_for('add_product'))
    return render_template("sell_product.html", product_sale_form=product_sale_form)


if __name__ == '__main__':
    app.run(debug=True)