import requests

# Wrap as a function which we can import as a module
from pathlib import Path
path = Path(__file__).parent / "../app_id.txt"
with path.open() as f:
    key = open(path, 'r').read()

if not key:
    print("You must have a valid API ID from openweathermap.org in order to query OpenWeatherMap.")
else:
    weather_base_url = "http://api.openweathermap.org/data/2.5/weather?"
    units = "imperial"

    #TODO: zip code should be passed in as a parameter by the caller.  Only if run directly should we prompt the user.
    #zip = input("Enter ZIP Code: ")

    #zip hard coded for dev testing
    zip = "92069"

    api_call = weather_base_url + "units=" + units + "&zip=" + zip + "&appid=" + key

    resp = requests.get(api_call).json()
    # End func wrapper

#TODO: "__main__" do not execute the following code if it is called as a module.  Allow the caller to handle parsing json and output formatting

if __name__ == "__main__":
    print()
    print(f"Executing API call:")
    print(f"{api_call}")

    print()
    print("Full json response:")
    print(resp)

    weather = resp["weather"][0]["main"]
    temp = resp["main"]["temp"]
    feels_like = resp["main"]["feels_like"]

    print()
    print(f"Current weather conditions for zip code {zip}")
    print(f"{weather}")
    print(f"Temperature: {temp}")
    print(f"Feels Like: {feels_like}")
