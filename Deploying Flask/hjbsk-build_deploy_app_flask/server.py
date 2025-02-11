from flask import Flask, render_template, request
from Maths.mathematics import summation,subtraction,multiplication
# Import the Maths package here

app = Flask("Mathematics Problem Solver")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/sum")
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    result = summation(num1,num2)
    return str(result)

@app.route("/sub")
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    result = subtraction(num1,num2)
    return str(result)

@app.route("/mul")
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here 
    result = multiplication(num1,num2)
    return str(result)

'''
@app.route("/")
def render_index_page():
    # Write your code here
'''
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
