from flask import Flask, render_template
import json
app = Flask(__name__)


@app.route('/')
def index():
    with open('articles.json','r') as file:
        articles = json.load(file)
    return render_template('index.html',articles = articles)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)