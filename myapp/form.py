# request を import に追加する
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def show():
    message = "hello world"
    return render_template("form.html", message = message)

@app.route("/result", methods=["POST"])
def result():
    message = "This is paiza"
    article = request.form["article"]
    # この下で、name変数に値を代入する
    name = request.form["name"]
    
    # テンプレートに、値を代入したname変数を渡す
    return render_template("form.html", message = message, article = article, name = name)

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")