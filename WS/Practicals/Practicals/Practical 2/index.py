from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Friends(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)

db.create_all()

@app.route('/')
def index():

    friend = db.session.query(Friends).all()
    return render_template('index.html', friends = friend)

@app.route('/add_friend', methods = ['GET', 'POST'])
def add_friend():
    return "reached"
    id = request.form["id"]
    names = request.form["name"]
     
    f = Friends(id = id, name = names)

    try:
        db.session.add(f)
        db.session.commit()

        data = db.session.query(Friends).all()
        print(data)
        return redirect('/')
    except Exception as e:
        return e

@app.route('/get_friend', methods = ['GET', 'POST'])
def get_friend():
    id = request.form["id"]
    name = db.session.query(Friends).filter_by(id = id).first()
    print(name)
    return redirect('/')

if __name__ == "__main__":
    app.run()