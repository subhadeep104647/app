from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "subho" and password == "123":
        return render_template("home.html", name=username)
    
    """else:
        return "invalid !"""
    
if __name__ == "__main__":
    app.run(debug=True)
