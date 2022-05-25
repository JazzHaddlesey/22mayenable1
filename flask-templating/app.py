from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello</h1>"

@app.route("/names")
def names():
    return render_template('names.html', names=['ben', 'harry', 'bob', 'jay', 'matt', 'bill'])

@app.route('/ben')
def ben():
    return render_template('ben.html')

@app.route('/harry')
def harry():
    return render_template('harry.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
