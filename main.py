from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

test_data = []

@app.route('/register', methods=['POST'])
def register_user():
    user_data = request.get_json()
    return jsonify({'message': 'User registered successfully'})


@app.route('/heart_rate/<user_id>', methods=['GET'])
def get_heart_rate(user_id):
    user_data = next((data for data in test_data if data['user_id'] == user_id), None)
    if user_data:
        average_bpm = user_data['bpm']
        heart_rate_zone = determine_heart_rate_zone(average_bpm)
        return jsonify({'heart_rate': average_bpm, 'heart_rate_zone': heart_rate_zone})
    else:
        return jsonify({'message': 'User not found'}), 404


@app.route('/heart_rate/update', methods=['POST'])
def update_heart_rate():
    heart_rate_data = request.get_json()
    user_id = heart_rate_data['user_id']
    current_bpm = heart_rate_data['bpm']
    heart_rate_zone = determine_heart_rate_zone(current_bpm)
    user_data = next((data for data in test_data if data['user_id'] == user_id), None)
    if user_data:
        user_data['bpm'] = current_bpm
    else:
        user_data = {'user_id': user_id, 'bpm': current_bpm}
        test_data.append(user_data)
    return jsonify({'message': 'Heart rate updated successfully', 'heart_rate_zone': heart_rate_zone})


def determine_heart_rate_zone(bpm):
    if bpm < 60:
        return 'Blue Zone (Resting Heart Rate)'
    elif bpm <= 100:
        return 'Green Zone (Normal Heart Rate)'
    else:
        return 'Red Zone (Elevated Heart Rate)'


if __name__ == '__main__':
    filename = 'test_data.json'
    counter = 1
    while os.path.exists(filename):
        counter += 1
        filename = f'test{counter}_data.json'
    
    # Load the initial test data from the JSON file
    with open('test_data.json') as file:
        test_data = json.load(file)
    
    with open(filename, 'w') as file:
        json.dump(test_data, file)
    
    app.run(debug=True)