from flask import Flask, render_template, request, redirect, url_for

from data.weather import get_weather
from data.base import create_db
from data.models import Pizza, Ingredient
from data.base import Session
from data import functions


app = Flask(__name__)


@app.get("/")
def index():
    weather = get_weather("New York")

    pizza_recom = ""
    if weather.get("temp") < 0:
        pizza_recom = "Неаполітано"
    elif weather.get("temp") > 40:
        pizza_recom = "Холодна піца"
    elif 0 <= weather.get("temp") < 20:
        pizza_recom = "Класична"
    else:
        pizza_recom = "Грибна"

    with Session() as session:
        pizzas = session.query(Pizza).all()

        return render_template("index.html", weather=weather, pizza_recom=pizza_recom, pizzas=pizzas)


@app.get("/poll/")
def poll():
    with Session() as session:
        pizzas = session.query(Pizza).all()
        return render_template("poll.html", pizzas=pizzas)


@app.get("/add_vote/")
def add_vote():
    pizza = request.args.get("vote")
    if not pizza:
        return redirect(url_for("poll"))

    functions.write_file(pizza)
    return redirect(url_for("results"))


@app.get("/results/")
def results():
    answers = functions.read_file()
    return render_template("results.html", answers=answers)


if __name__ == "__main__":
    create_db()
    app.run(debug=True,port=5001)
