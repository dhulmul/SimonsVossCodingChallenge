from flask import Flask, jsonify, request, redirect, render_template, flash
from forms import SearchForm
from search.import_json import get_objects_handler, get_top_k_results
import os

app = Flask(__name__)
app.secret_key = "not a secret key"


buildings_obj, locks_obj, groups_obj, media_obj = get_objects_handler()


@app.route('/',  methods=['GET', 'POST'])
def hello_world():
    search = SearchForm(request.form)
    if request.method == 'POST':
        print(search.query.data)
        return search_results(search)
    return render_template('index.html', form=search)


@app.route('/results', methods=['GET', 'POST'])
def search_results(search):
    results = get_top_k_results(buildings_obj, locks_obj, groups_obj, media_obj, search.query.data, 20)
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        return render_template('results.html', results=results)


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 7000))
    print("PORT ", PORT)
    app.run(host='0.0.0.0', debug=True, port=PORT)
