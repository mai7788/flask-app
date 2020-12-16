from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return "ok"
    return render_template('index.html')

@app.route('/article')
def article():
    return render_template('generic.html')

@app.route('/element')
def element():
    return render_template('elements.html')

