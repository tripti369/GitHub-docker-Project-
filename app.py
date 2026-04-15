from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    result = None
    error = None
    expression = ''

    if request.method == 'POST':
        try:
            num1 = float(request.form.get('num1', ''))
            num2 = float(request.form.get('num2', ''))
            op = request.form.get('operation')

            symbols = {'add': '+', 'sub': '-', 'mul': '×', 'div': '÷'}
            operator = symbols.get(op, '?')
            expression = f"{num1} {operator} {num2}"

            if op == 'add':
                result = num1 + num2
            elif op == 'sub':
                result = num1 - num2
            elif op == 'mul':
                result = num1 * num2
            elif op == 'div':
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2
            else:
                error = 'Please choose a valid operation.'
        except ValueError:
            error = 'Please enter valid numbers in both fields.'
        except ZeroDivisionError:
            error = 'Division by zero is not allowed.'

    return render_template('main.html', result=result, error=error, expression=expression)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
