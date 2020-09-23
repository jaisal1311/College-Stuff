from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#Initializing Flask App
app = Flask(__name__)

# For Hot reload
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Initializing SQLite usong SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# Initiating db
db = SQLAlchemy(app)

# Creatnig the Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    completed = db.Column(db.Integer, default = 0)
    date = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task ' + self.id + '>' 

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == "POST":
        content = request.form['content']
        new_task = Todo(content = content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return "Err"
    tasks = Todo.query.order_by(Todo.date).all()
    return render_template('index.html', tasks = tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_delete = Todo.query.get_or_404(id)

    db.session.delete(task_delete)
    db.session.commit()
    return redirect('/')

@app.route('/edit/<int:id>', methods = ['GET', 'POST'])
def edit(id):
    task = Todo.query.get_or_404(id)

    if request.method == "POST":
        task.content = request.form["content"]

        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit.html', task = task)
        
if __name__ == "__main__":
    app.run()