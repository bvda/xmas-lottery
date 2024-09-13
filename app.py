from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['POST'])
def get_data():
    # Extracting some data from the AJAX request
    input_data = request.json.get('input', None)
    
    # Sending a JSON response
    if input_data:
        return jsonify({'response': f'You sent: {input_data}'})
    else:
        return jsonify({'response': 'No input received'}), 400

if __name__ == '__main__':
    app.run(debug=True)
