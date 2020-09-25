from flask import Flask, render_template, request
from zeep import Client

url = 'http://localhost:51948/WebService1.asmx?WSDL'
client = Client(url)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods = ["POST"])
def add():
    x = request.form['num1']
    y = request.form['num2']
    s = client.service.Add(x, y)
    return str(s)

@app.route('/multi', methods = ["POST"])
def multi():
    x = request.form['num1']
    y = request.form['num2']
    s = client.service.Multi(x, y)
    return str(s)

if __name__ == "__main__":
    app.debug = True
    app.run()