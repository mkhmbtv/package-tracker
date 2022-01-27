from flask import Flask, redirect, render_template, request, url_for
from app.config import Config
from app.shipping_form import ShippingForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return 'Package Tracker'


@app.route('/new_package', methods=['GET', 'POST'])
def add_package():
    form = ShippingForm()
    if request.method == 'POST':
        if form.cancel.data:
            return redirect(url_for('.add_package'))
    if form.validate_on_submit():
        return redirect(url_for('.index'))
    return render_template('shipping_request.html', form=form)
