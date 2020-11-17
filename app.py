from flask import Flask
from db.dao import query
app = Flask(__name__)


@app.route('/')
def hello():
    """
    docstring
    """
    return query()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
