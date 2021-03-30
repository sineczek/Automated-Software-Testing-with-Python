from flask import Flask, render_template, request

app = Flask(__name__)
transactions = [
    ("2021-03-05", 70.00, "Checking"),
    ("2021-03-21", 94.96, "Savings"),
    ("2021-03-26", 120.00, "Checking"),

]

@app.route("/", methods=["GET", "POST"])
def home():
    print(request.args)
    # print(request.form.get("account")) #bierze nazwę pola i zwraca jej wartość
    if request.method == "POST":
        transactions.append(
            (
                request.form.get("date"),
                float(request.form.get("ammount")),
                request.form.get("account"),
            )
        )
    return render_template("form.html")

@app.route("/transactions")
def show_transactions():
    return render_template("transactions.jinja2", entries = transactions)


# jinja2 - templatinglanguage