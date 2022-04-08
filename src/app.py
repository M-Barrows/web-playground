from flask import Flask, render_template

app = Flask(__name__)

@app.route('/status')
def hello():
    return 'Hello World!',200

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__': 
    app.run(debug=True)