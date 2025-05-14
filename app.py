from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/secret")
def secret_page():
    return render_template("secret.html")

@app.route("/internal-api")
def internal_api():
    return render_template("internal_api.html")

@app.route("/internal-secret")
def internal_secret():
    return render_template("internal_secret.html")

@app.route("/redirect")
def redirector():
    target = request.args.get("to")
    return '', 302, {'Location': target}

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/lab1", methods=["GET", "POST"])
def lab1():
    content = ""
    if request.method == "POST":
        url = request.form.get("url")
        try:
            response = requests.get(url, timeout=3, allow_redirects=True)
            content = response.text
        except Exception as e:
            content = f"Error: {e}"
    return render_template("lab1.html", content=content)

@app.route("/lab2", methods=["GET", "POST"])
def lab2():
    content = ""
    if request.method == "POST":
        url = request.form.get("url")
        try:
            response = requests.get(url, timeout=3, allow_redirects=True)
            content = response.text
        except Exception as e:
            content = f"Error: {e}"
    return render_template("lab2.html", content=content)

@app.route("/lab3", methods=["GET", "POST"])
def lab3():
    content = ""
    if request.method == "POST":
        url = request.form.get("url")
        try:
            response = requests.get(url, timeout=3, allow_redirects=True)
            content = response.text
        except Exception as e:
            content = f"Error: {e}"
    return render_template("lab3.html", content=content)

@app.route("/fetch", methods=["POST"])
def fetch():
    url = request.form.get("url")
    try:
        response = requests.get(url, allow_redirects=True, timeout=3)
        return f"<pre>{response.text}</pre>"
    except Exception as e:
        return f"<pre>Error: {e}</pre>"

if __name__ == "__main__":
    app.run(debug=True)