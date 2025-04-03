import sys
print(f"Path: {sys.path}\n")
sys.path.insert(0, "C:\\repos\\github\\python_utils\\OpenWeatherMap_org\\get_weather") #"get_weather" folder
print(f"Path: {sys.path}\n")

from flask import Flask, jsonify, request
from get_weather import OpenWeatherMap

app = Flask(__name__)

def get_weather_by_zip(zip_code):
    resp = OpenWeatherMap.GetWeatherByZip(zip_code)
    if resp["cod"] == 200:
        return resp
    else:
        print(f"Error: ({resp["cod"]}) {resp["message"]}")
        return resp

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify({'items': ['item1', 'item2', 'item3']})

@app.route('/api/weather', methods=['GET'])
def weather():
    #sample use: "http://127.0.0.1:5000/api/weather?zip_code=77386"
    #get zip code from the user
    zip = request.args.get('zip_code')
    return get_weather_by_zip(str(zip))

if __name__ == '__main__':
    app.run(debug=True)
