from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prac.db'

db = SQLAlchemy(app)

class Friend(db.Model):
    name = db.Column(db.String(100))
    rn = db.Column(db.Integer(), primary_key = True)

    def __init__(self, name, rn):
        self.name = name
        self.rn = rn

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html', friend = Friend.query.all())
    else:
        friend = Friend(name = request.form['name'], rn = request.form['rn'])
        try:
            db.session.add(friend)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return 'Something\'s Fishy\n' + str(e)
            
@app.route('/del/<int:rno>', methods = ['GET', 'POST'])
def delete(rno):
    d = Friend.query.get_or_404(rno)
    try:
        db.session.delete(d)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return ('Something\'s fishy\n' + str(e))

@app.route('/edit/<int:rno>', methods=['GET', 'POST'])
def update(rno):
    d = Friend.query.get_or_404(rno)

    if request.method == 'POST':
        d.name = request.form['name']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return ('There was an issue updating your task')

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)
