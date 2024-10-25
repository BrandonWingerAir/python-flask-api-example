from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Route'

@app.route('/songs')
def get_songs():
    return {"songs": "songs data"}