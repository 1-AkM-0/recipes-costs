from flask import Flask, redirect, render_template, request
import sqlite3

app = Flask(__name__)

def tuple_dict(query, db):
    result = [dict(query) for query in db.fetchall()]
    return result



app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


con = sqlite3.connect("database.db", check_same_thread=False)
con.row_factory = sqlite3.Row
db = con.cursor()

@app.route("/")
def index():

    return render_template("index.html")



@app.route("/inputs", methods=["GET", "POST"])
def inputs():
    inputs = db.execute("SELECT * FROM inputs")
    inputs = tuple_dict(inputs, db)
    return render_template("inputs.html", inputs=inputs)


@app.route("/products", methods=["GET", "POST"])
def products():
    if request.method == "POST":
        name = request.form.get("name")
        category = request.form.get("category")
        quantity = request.form.get("quantity")
        unit = request.form.get("unit")
        cost = request.form.get("cost")

        if not name:
            return(1)
        if not category:
            return(1)
        if not quantity:
            return 1
        if not unit:
            return 1
        if not cost:
            return 1
        
        unit_cost = (float(cost) / int(quantity))
        
        
        db.execute('''
                   INSERT INTO produtos (nome, categoria, volume_bruto, un_medida, custo_medio, custo_un)
                   VALUES (?, ?, ?, ?, ?, ?)''', (name, category, quantity, unit, cost, unit_cost) )
        
        con.commit()
        

    products = db.execute ("SELECT * FROM produtos")
    products = tuple_dict(products, db)

    return render_template("products.html", products=products)


if __name__ == "__main__":
    app.run(debug=True)



