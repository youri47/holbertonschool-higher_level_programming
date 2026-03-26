#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

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


def read_sql(db_path, product_id=None):
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        if product_id:
            cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
        else:
            cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        data = [dict(row) for row in rows]
        conn.close()
        return data
    except sqlite3.Error:
        return None


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        products = read_json('products.json', product_id)
    elif source == 'csv':
        products = read_csv('products.csv', product_id)
    elif source == 'sql':
        products = read_sql('products.db', product_id)
        if products is None:
            return render_template('product_display.html', error="Database error")
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id and not products:
        return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
