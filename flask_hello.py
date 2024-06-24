from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the AI course!'

@app.route('/world')
def helo():
    return 'hello world'

if __name__ == '__main__' :
    app.run(debug= True)

