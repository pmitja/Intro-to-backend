from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/fakebook")
def fakebook():
    return render_template("index_fakebook.html")


@app.route("/hairdresser_hans")
def hairdresser():
    return render_template("index_hairdresser_hans.html")

if __name__ == '__main__':
    app.run()