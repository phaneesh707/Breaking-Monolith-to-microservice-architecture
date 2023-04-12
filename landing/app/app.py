from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def extract_result(response):
    result = -1
    try:
        result = response.json()['result']
    except:
        error = "An error occured while extracting the result"
        print(error)
        result = error
    return result

@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = 0.0
    number_2 = 0.0
    new_num_1 = 0.0
    new_num_2 = 0.0
    number_1_sign = 1
    number_2_sign = 1
    flag = 0
    try:
        number_1 = float(request.form.get("first"))
        number_2 = float(request.form.get('second'))
        new_num_1 = number_1
        new_num_2 = number_2
        if(number_1 == -0):
            number_1 = 0.0
        if(number_2 == -0):
            number_2 = 0.0
        
        if(number_1 < 0):
            number_1_sign = 0
        if(number_2 < 0):
            number_2_sign = 0
        number_1 = abs(number_1)
        number_2 = abs(number_2)
     
    except:
        print("Ntg is passed")
        flag = 1
    
    operation = request.form.get('operation')
    result = 0

    if operation == 'add':
        response = requests.get(f'http://addition-service:5051/add/{number_1}/{number_2}/{number_1_sign}/{number_2_sign}')
        result = extract_result(response)

    elif operation == 'divide':
        response = requests.get(f'http://division-service:5052/div/{number_1}/{number_2}/{number_1_sign}/{number_2_sign}')
        result = extract_result(response)

    elif operation == 'equalto':
        response = requests.get(f'http://equalto-service:5053/equalto/{number_1}/{number_2}/{number_1_sign}/{number_2_sign}')
        result = extract_result(response)

    elif operation == 'greater':
        response = requests.get(f'http://greater-service:5054/greater/{number_1}/{number_2}/{number_1_sign}/{number_2_sign}')
        result = extract_result(response)
    
    elif operation == 'lesser':
        response = requests.get(f'http://lesser-service:5055/lesser/{number_1}/{number_2}/{number_1_sign}/{number_2_sign}')
        result = extract_result(response)

    elif operation == 'multiply':
        response = requests.get(f'http://multiplication-service:5056/mul/{number_1}/{number_2}/{number_1_sign}/{number_2_sign}')
        result = extract_result(response)
    
    elif operation == 'minus':
        response = requests.get(f'http://substraction-service:5057/sub/{number_1}/{number_2}/{number_1_sign}/{number_2_sign}')
        result = extract_result(response)
    
    if flag == 0:
        flash(f'The result of operation {operation} on {new_num_1} and {new_num_2} is {result}')
    else:
        flash(f'Please enter both the input fields before submitting')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )