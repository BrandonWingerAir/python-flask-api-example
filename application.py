from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Setlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    songs = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.songs}"

@app.route('/')
def index():
    return 'Index Route'

@app.route('/setlists')
def get_setlists():
    setlists = Setlist.query.all()

    output = []
    for setlist in setlists:
        setlist_data = {'name': setlist.name, 'songs': setlist.songs}

        output.append(setlist_data)

    return {"setlists": setlist_data}

@app.route('/setlists/<id>')
def get_setlist(id):
    setlist = Setlist.query.get_or_404(id)
    return {"name": setlist.name, "songs": setlist.songs}