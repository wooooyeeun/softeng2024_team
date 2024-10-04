from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title="Portfolio")

app.run(debug=True)

