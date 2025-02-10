from flask import Blueprint, render_template

views = Blueprint('views', __name__, template_folder='templates')

# Homepage
@views.route('/')
def home(): # called at localhost:5500/
    return render_template('base.html')