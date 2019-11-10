from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'SimonsVoss Search App!'


@app.route('/search', methods=['GET'])
def search():
    results = es.get(index='')
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
