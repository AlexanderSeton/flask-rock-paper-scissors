# from flask import render_template
from app import app

@app.route("/<choice1>/<choice2>")
def index(choice1, choice2):
    return "Hello"
