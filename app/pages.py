from flask import Blueprint, render_template

# Zdefiniowanie blueprintu dla frontu
bp = Blueprint("pages", __name__)

# Strona startowa
@bp.route("/")
def home():
    return render_template("pages/home.html")
