from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ("hello world, index")

@app.route('/mike')
def mike():
    n1 = 10
    n2 = 20
    return ("hello world, Mike")

if __name__ == '__main__':
    app.run(debug=True)