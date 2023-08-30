from flask import Flask, render_template


app = Flask(__name__)

JOB = [
    {
        id: 1,
        'title': 'Software Engineer',
        'location': 'San Francisco, CA',
        'salary': '$100,000',
    },
    {
        id: 2,
        'title': 'data scientist',
        'location': 'cairo, egypt',
        'salary': '$50,000',
    },
    {
        id: 3,
        'title': 'data engineer',
        'location': 'USA, CA',
        'salary': '$150,000',
    },
    {
        id: 4,
        'title': 'front end developer',
        'location': 'UAE, Dubai',
        'salary': '$200,000',
    },
        
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOB, campany_name="Bakry")
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)