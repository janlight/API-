from flask import Blueprint, render_template,request
import pickle
bp = Blueprint('main', __name__, url_prefix='/main')

@bp.route('/',strict_slashes=False)
def home():
    return render_template('main.html',image_file="image/pulse2.jpg")