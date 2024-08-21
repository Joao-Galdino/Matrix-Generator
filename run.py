from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    rows = int(request.form.get('rows', 5))
    cols = int(request.form.get('cols', 5))
    matrix = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
    
    zeros = sum(row.count(0) for row in matrix)
    ones = sum(row.count(1) for row in matrix)
    total = zeros + ones
    
    zero_percent = (zeros / total) * 100
    one_percent = (ones / total) * 100
    
    result = {
        'matrix': matrix,
        'zeros': zeros,
        'ones': ones,
        'total': total,
        'zero_percent': round(zero_percent, 2),
        'one_percent': round(one_percent, 2),
        'more_frequent': 'zeros' if zeros > ones else 'ones' if ones > zeros else 'equal'
    }
    return render_template('matrix_result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
