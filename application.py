from flask import Flask, request, jsonify
from nsetools import Nse
from parser import Parser

app = Flask(__name__)
parse = Parser()

@app.route('/health')
def health_check():
    return "I am Alive"

@app.route('/stock/<name>', methods=['GET'])
def get_stock_name(name):
    queries = request.args.getlist('query')
    print(f"the value of queries is : {queries}")

    obj = parse.quote_by_stock_name(name, queries)
    return jsonify(obj)

@app.route('/stock/gainers', methods=['GET'])
def get_top_gainers():
    obj = parse.get_top_gainers()
    return jsonify(obj)

