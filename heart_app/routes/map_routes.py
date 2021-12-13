from flask import Blueprint, render_template
import os

from dotenv import load_dotenv, find_dotenv


bp = Blueprint('map', __name__, url_prefix='/map')

@bp.route('/')
def map():
    
    return render_template('map.html')


