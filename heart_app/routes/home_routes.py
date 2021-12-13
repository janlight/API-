from flask import Blueprint, render_template
import pickle
bp = Blueprint('/', __name__)

@bp.route('/')
def home():
    return render_template('home.html')