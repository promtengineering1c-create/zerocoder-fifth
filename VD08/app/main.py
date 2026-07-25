from flask import Blueprint, render_template, request
from .services import get_quote

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():

    quote = None
    if request.method == 'POST':
        quote = get_quote()

    return render_template('index.html', quote=quote)