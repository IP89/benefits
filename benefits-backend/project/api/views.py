from flask import Blueprint, jsonify


benefits_blueprint = Blueprint('benefits', __name__, template_folder='./templates')
@benefits_blueprint.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        db.session.add(User(username=username, email=email))
        db.session.commit()

    users = User.query.all()
    return render_template('index.html', users=users)