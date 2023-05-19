from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        data = request.get_json()
        
        # Extract the required data from the request JSON
        status = 'Success'  # Set your desired status value
        user_id = data.get('user_id')
        email_id = data.get('email_id')
        roll_number = data.get('roll_number')
        numbers = data.get('numbers')
        alphabets = data.get('alphabets')
        
        # Prepare the response JSON
        response = {
            'status': status,
            'user_id': user_id,
            'email_id': email_id,
            'roll_number': roll_number,
            'numbers': numbers,
            'alphabets': alphabets
        }
        
        return jsonify(response)
    else:
        # GET request handler
        operation_code = 'XYZ'  # Set your desired operation code value
        return jsonify({'operation_code': operation_code})

if __name__ == '__main__':
    app.run(debug=True)
