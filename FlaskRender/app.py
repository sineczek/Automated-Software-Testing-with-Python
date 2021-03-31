from flask import Flask, render_template, request  # do flsk koniecnze pip install flask
import psycopg2

app = Flask(__name__)
transactions = [
    ("2021-03-05", 70.00, "Checking"),
    ("2021-03-21", 94.96, "Savings"),
    ("2021-03-26", 120.00, "Checking"),

]
POSTGRESQL_URI = "postgres:// -- cut --"  # do integracji konieczny pip install psycopg2-binary

connection = psycopg2.connect(POSTGRESQL_URI)
try:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("CREATE TABLE transactions (date TEXT, amount REAL, account TEXT);")  # 1 tabela, 3 kolumny
except psycopg2.errors.DuplicateTable:
    pass


@app.route("/", methods=["GET", "POST"])
def home():
    print(request.args)
    # print(request.form.get("account")) #bierze nazwę pola i zwraca jej wartość
    if request.method == "POST":
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO transactions VALUES (%s, %s, %s);"
                        (
                        request.form.get("date"),
                        float(request.form.get("ammount")),
                        request.form.get("account"),
                    ),
                )
    return render_template("form.html")


@app.route("/transactions")
def show_transactions():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM transactions;")
            transactions = cursor.fetchall()
    return render_template("transactions.jinja2", entries=transactions)

# jinja2 - templatinglanguage
