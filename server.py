from flask import Flask
from flask import render_template

import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', 
    	rnd=random.randint(1,6))

@app.route('/koodauskerho')
def koodauskerho():
    return '????'

if __name__ == "__main__":
    app.run()