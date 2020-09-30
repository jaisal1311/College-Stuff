from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prac.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Friends(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))

    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods = ["POST", "GET"])
def add():
    friend = Friends(uid = request.form['uid'], name = request.form['name'])

    db.session.add(friend)
    db.session.commit()

    return redirect('/')

@app.route('/search', methods = ['POST', 'GET'])
def search():
    if request.method == 'POST':
        friend = Friends.query.filter_by(uid = request.form['uid']).first()
        return json.dumps({'freinds': {'uid': request.form['uid'], 'name': friend.name}})

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)
