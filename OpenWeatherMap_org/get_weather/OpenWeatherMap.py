import requests
from pathlib import Path

_weather_base_url = "http://api.openweathermap.org/data/2.5/weather?"
_units = "imperial"

def GetAppId():
    #Requires the file app_id.txt exists.  The only contents of this file are the AppId provided by OpenWeatherMap.com.
    path = Path(__file__).parent / "../app_id.txt"
    with path.open() as f:
        key = open(path, 'r').read()
    return key


def GetWeatherByZip(zip):
    app_id = GetAppId()
    api_call = _weather_base_url + "units=" + _units + "&zip=" + zip + "&appid=" + app_id

    resp = requests.get(api_call).json()
    return resp


def GetWeatherByCityStateCountry(city, state, country):
    app_id = GetAppId()
    api_call = _weather_base_url + "units=" + _units + "&appid=" + app_id + "&q=" + city 

    #Add state if not empty
    if len(state) > 0:
        api_call += f",{state}"
        
    #add country if not empty
    if len(country) > 0:
        api_call += f",{country}"
    
    resp = requests.get(api_call).json()
    return resp
