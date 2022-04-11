from flask import Flask, render_template

app = Flask(__name__)

@app.route('/status')
def hello():
    return 'Hello World!',200

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/leaderboard')
def leaderboard():
    visits = [
        {
            'name':'Michael',
            'visits':3
        },
        {
            'name':'Joe',
            'visits':2
        },
        {
            'name':'Billy',
            'visits':1
        }
    ]

    streak = [
        {
            'name':'Michael',
            'streak':2
        },
        {
            'name':'Joe',
            'streak':1
        },
        {
            'name':'Billy',
            'streak':3
        }
    ]

    return render_template('leaderboard.html',visits = visits, streak = streak)
if __name__ == '__main__': 
    app.run(debug=True)