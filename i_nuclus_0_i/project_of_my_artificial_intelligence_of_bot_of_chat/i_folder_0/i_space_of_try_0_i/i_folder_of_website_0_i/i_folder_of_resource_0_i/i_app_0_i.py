













from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/i_example_0_i")
def i_example_0_i():
    return render_template("index.html")


@app.route("/about")
def about():
    return "<h1>About My Website</h1><p>This page uses Flask.</p>"


if __name__ == "__main__":
    app.run(debug=True)











