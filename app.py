from flask import Flask, render_template, jsonify, request
from lottery import Lottery

app = Flask(__name__)
lottery = Lottery()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_draw', methods=['GET'])
def get_draw():
    return jsonify({'response': lottery.draw()})

@app.route('/get_data', methods=['POST'])
def get_data():
    # Extracting some data from the AJAX request
    # input_data = request.json.get('input', None)

    # return render_template('index.html')

    return jsonify({'response': lottery.get_pool()})

if __name__ == '__main__':
    app.run(debug=True)
