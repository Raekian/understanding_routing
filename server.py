from flask import Flask
app = Flask(__name__)





@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/<string>')
def say(string):
    return "Hi " + string

@app.route('/repeat/<string>/<int:number>')
def repeat(string, number):
    result = string *number
    return result


if __name__=="__main__":
    app.run(debug=True)

