import pickle
import json
import numpy as np

__city = None
__data_columns = None
__model = None

def get_estimated_price(city,sqft_living,sqft_lot,floors,sqft_above):
    try:
        loc_index = __data_columns.index(city.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft_living
    x[1] = sqft_lot
    x[2] = floors
    x[3] = sqft_above
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],3)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __city

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __city = __data_columns[4:]

    global __model
    if __model is None:
        with open('./artifacts/house_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __city

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Bothell',1300, 7349, 2,3000))
    print(get_estimated_price('Shoreline',1600, 4349, 1,1500))