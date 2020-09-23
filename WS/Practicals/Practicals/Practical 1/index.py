from flask import Flask, render_template, request

app = Flask('__name__')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/f_to_c", methods=["POST"])
def f_c():
    num1 = float(request.form["num1"])
    return "fahrenheit to celsius: " + str(((num1 - 32) * (5 / 9)))

@app.route("/c_to_f", methods=["POST"]) 
def c_f():
    num1 = float(request.form["num1"])
    return "celsius to fahrenheit: " + str((num1*(9/5) + 32))

if __name__ == "__main__":
    app.run()