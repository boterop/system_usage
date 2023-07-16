from lib.system import System
from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.get('/system-usage')
def system_usage():
    return System.get_all()


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
