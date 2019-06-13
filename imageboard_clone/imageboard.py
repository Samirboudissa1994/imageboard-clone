from flask import Flask
app = Flask(__name__)


@app.route("/")
def imageboard():
    return "This will be an imageboard"


if __name__ == '__main__':
    app.run(debug=True)
