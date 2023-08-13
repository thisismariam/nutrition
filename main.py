from flask import Flask, render_template, request, redirect, g
import csv
import sqlite3

app = Flask(__name__)

DATABASE = 'nutrition.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search", methods=["POST"])
def search():
    food_item = request.form["food-item"]

    # Retrieve data from the SQL database based on a partial match using the LIKE operator
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Nutritiontable WHERE name LIKE ?", ('%' + food_item + '%',))
    results = cursor.fetchall()
    conn.close()

    if results:
        return render_template("results.html", data=results)
    else:
        return "No matching food items found."

if __name__ == "__main__":
    app.run()
