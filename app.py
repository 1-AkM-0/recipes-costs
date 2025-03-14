from flask import Flask, redirect, render_template, request
import sqlite3

app = Flask(__name__)




app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


con = sqlite3.connect("database.db")
db = con.cursor()

@app.route("/")
def index():

    return render_template("index.html")



@app.route("/inputs", methods=["GET", "POST"])
def inputs():
    
    return render_template("inputs.html")


@app.route("/products", methods=["GET", "POST"])
def products():
    return render_template("products.html")



if __name__ == "__main__":
    app.run(debug=True)



