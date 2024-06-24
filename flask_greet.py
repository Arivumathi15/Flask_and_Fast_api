from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')  # Get the 'name' parameter from the query string
    greeting = f"Hello, {name}!"
    # return jsonify({'message': greeting})
    return greeting

if __name__ == '__main__':
    app.run(debug=True)

# def greet(name):
#     return f"Hello, {name}!"

