from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def imageboard():
    return render_template('home.html')


@app.route("/b/")
def random():
    return render_template('random.html')


if __name__ == '__main__':
    app.run(debug=True)
