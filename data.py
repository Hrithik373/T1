import json
import random
from datetime import datetime, timedelta
import time
import os

def generate_test_data():
    bpm = random.randint(50, 120)  # Random BPM between 50 and 120
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    data_entry = {'timestamp': timestamp, 'bpm': bpm}
    
    return data_entry

# Generate test data for 1 minute (6 data entries) and save it to a JSON file
num_entries = 6  # Number of data entries to generate
test_data = []

for i in range(num_entries):
    data_entry = generate_test_data()
    test_data.append(data_entry)
    
    # Wait for 10 seconds
    time.sleep(5)

# Determine the file name based on the current count
file_count = 1  # Initial file count
file_name = f'test{file_count}_data.json'

# Find the next available file name by incrementing the count
while file_name in os.listdir('.'):
    file_count += 1
    file_name = f'test{file_count}_data.json'

# Save the test data to the JSON file
with open(file_name, 'w') as file:
    json.dump(test_data, file, indent=4)

print(f'Test data saved to: {file_name}')