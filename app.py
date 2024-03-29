from flask import Flask
from buzz import generator
import os

app = Flask(__name__)


@app.route("/")
def generate_buzz():
    page = '<html><body><h2>'
    page += generator.generate_buzz()
    page += '</h2></body></html>'
    return page


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))