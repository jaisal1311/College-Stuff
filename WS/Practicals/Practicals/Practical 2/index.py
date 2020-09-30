from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class Friends(db.Model):
    Id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))

    def __init__(self, Id, name):
        self.Id = Id
        self.name = name
        
@app.route('/')
def show_all():
   return render_template('show_all.html')

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == "POST":
        if not request.form['Id'] or not request.form['name']:
            flash("Please fill all details properly", "error")
        else:
            friend = Friends(Id = request.form['Id'], name = request.form['name'])

            db.session.add(friend)
            db.session.commit()

            return redirect(url_for('show_all'))
        
    return render_template('new.html')

@app.route('/search', methods = ['GET', 'POST'])
def search():
    if request.method == "POST":
        i = request.form['Id']
        fr = Friends.query.filter_by(Id = i).first()
        d = {
            'Id': fr.Id,
            'Name': fr.name
        }
        return render_template('res.html', f = d)
            

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
