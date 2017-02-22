from flask import Flask, request, render_template
import fs


app = Flask(__name__)

# This displays the home page with the form
@app.route('/')
def home_page():
    return render_template('home.html')


# This runs in response to the form button clicked.
@app.route('/query_by_zip')
def search():
    zip_code = request.args.get('zip_code')

    # You'd most likely modify search_by_zip to return data in a more useful format for your web app
    results = fs.search_by_zip(zip_code)
    return render_template('results.html', results=results['response']['venues'])
