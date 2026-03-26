#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json(file_path, product_id=None):
    with open(file_path, 'r') as f:
        data = json.load(f)
    if product_id:
        data = [p for p in data if p['id'] == product_id]
    return data


def read_csv(file_path, product_id=None):
    data = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            data.append(row)
    if product_id:
        data = [p for p in data if p['id'] == product_id]
    return data


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        products = read_json('products.json', product_id)
    elif source == 'csv':
        products = read_csv('products.csv', product_id)
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id and not products:
        return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
