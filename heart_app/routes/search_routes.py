from flask import Blueprint, render_template,request

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/')
def search():
    return render_template('search.html',image_file="image/pulse.jpg")