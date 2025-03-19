import requests
from pathlib import Path


def GetAppId():
    path = Path(__file__).parent / "../app_id.txt"
    with path.open() as f:
        key = open(path, 'r').read()
    return key


def GetWeatherByZip(zip):
    app_id = GetAppId()

    weather_base_url = "http://api.openweathermap.org/data/2.5/weather?"
    units = "imperial"

    api_call = weather_base_url + "units=" + units + "&zip=" + zip + "&appid=" + app_id

    resp = requests.get(api_call).json()
    return resp


def GetWeatherByCityStateCountry(city, state, country):
    app_id = GetAppId()

    weather_base_url = "http://api.openweathermap.org/data/2.5/weather?"
    units = "imperial"

    api_call = weather_base_url + "units=" + units + "&appid=" + app_id + "&q=" + city 

    #Add state if not null
    if len(state) > 0:
        api_call += f",{state}"

    #add country if not null
    if len(country) > 0:
        api_call += f",{country}"

    resp = requests.get(api_call).json()

    return resp


# Only execute as a script not when imported
if __name__ == "__main__":
    resp = GetWeatherByZip("92069")

    weather = resp["weather"][0]["main"]
    temp = resp["main"]["temp"]
    feels_like = resp["main"]["feels_like"]

    print()
    print(f"Current weather conditions for zip code {zip}")
    print(f"{weather}")
    print(f"Temperature: {temp}")
    print(f"Feels Like: {feels_like}")
