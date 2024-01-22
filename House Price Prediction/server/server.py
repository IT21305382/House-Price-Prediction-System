from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'city': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    sqft_living = float(request.form['sqft_living'])
    city = request.form['city']
    sqft_lot = float(request.form['sqft_lot'])
    floors = float(request.form['floors'])
    sqft_above = float(request.form['sqft_above'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(city,sqft_living,sqft_lot,floors,sqft_above)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()