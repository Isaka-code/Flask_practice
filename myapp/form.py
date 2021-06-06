from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def show():
    message = "hello world"
    return render_template("form.html", message = message)