#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')  # Corrected from _route to route
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')  # Corrected from _route to route
def print_string(parameter):
    print(parameter)  # Print to console
    return parameter  # Display in web browser

@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join([str(i) for i in range(param)])
    return f'{numbers}\n'  # Add the trailing newline here



@app.route('/math/<int:num1>/<operation>/<int:num2>')  # Corrected from _route to route
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return str(result)  # Return the result as a string

if __name__ == '__main__':
    app.run(port=5555, debug=True)
