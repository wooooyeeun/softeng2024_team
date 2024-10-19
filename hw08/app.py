from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/blog')
def blog():
    df = pd.read_csv("data.csv")
    post_list = []
    for i, row in df.iterrows():
        post_list.append({
            "title": row['title'],
            "content": row['content']})
    return render_template('blog.html', title="blog post", posts=post_list)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title="Portfolio")

app.run(debug=True)

