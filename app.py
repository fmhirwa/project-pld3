from flask import Flask, render_template, request
import sqlite3
import sqlite3

conn = sqlite3.connect('/file.db')


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = []
    with sqlite3.connect('business.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM companies WHERE name LIKE ? OR description LIKE ?", ('%'+query+'%', '%'+query+'%'))
        results = cursor.fetchall()
    return render_template('search_results.html', query=query, results=results)

if __name__ == '_-Main__':
    app.run(debug=True)
