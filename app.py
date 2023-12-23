from flask import Flask, render_template, request, jsonify
import csv

app = Flask(__name__, static_url_path='/static')

# to read and display the uploaded data.csv file on the screen
@app.route('/')
def display_data():
    data = read_csv_file('data.csv')
    return render_template('index.html', data=data)

# creating selected food into a csv file
@app.route('/save_selected_items', methods=['POST'])
def save_selected_items():
    selected_items = request.json['selectedItems']
    save_to_csv('food.csv', selected_items)
    return jsonify({'message': 'Selected items saved successfully'})

# creating selected non-food into a csv file
@app.route('/save_selected_items1', methods=['POST'])
def save_selected_items1():
    selected_items = request.json['selectedItems1']
    save_to_csv('non-food.csv', selected_items)
    return jsonify({'message': 'Selected items 1 saved successfully'})
    
# creating selected utensils into a csv file
@app.route('/save_selected_items2', methods=['POST'])
def save_selected_items2():
    selected_items = request.json['selectedItems2']
    save_to_csv('utensils.csv', selected_items)
    return jsonify({'message': 'Selected items 2 saved successfully'})


# # creating newly added category into a csv file
# @app.route('/save_selected_items3', methods=['POST'])
# def save_selected_items3():
#     selected_items = request.json['selectedItems3']
#     save_to_csv('#NEWCATEGORY.csv', selected_items)
#     return jsonify({'message': 'Selected items 3 saved successfully'})


# to read data from a CSV file
def read_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data

# to save data to a CSV file
def save_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Selected Item'])
        for item in data:
            writer.writerow([item])

if __name__ == '__main__':
    app.run(debug=True)
