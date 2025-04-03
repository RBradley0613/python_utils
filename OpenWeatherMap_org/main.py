from get_weather import OpenWeatherMap
from datetime import datetime
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def DisplayResponse(resp):
    city_name = resp["name"]
    weather = resp["weather"][0]["main"]
    temp = resp["main"]["temp"]
    feels_like = resp["main"]["feels_like"]

    rise_time = resp["sys"]["sunrise"]
    set_time = resp["sys"]["sunset"]
    sunrise = datetime.fromtimestamp(rise_time)
    sunset = datetime.fromtimestamp(set_time)

    clear_screen()

    print()
    print(f"Current weather conditions for {city_name}")
    print()
    print(f"{weather}")
    print(f"Temperature: {temp}")
    print(f"Feels Like: {feels_like}")
    print()
    print(f"Sunrise at {sunrise.strftime("%I:%M %p")} local time")
    print(f"Sunset at {sunset.strftime("%I:%M %p")} local time")
    print()

if __name__ == "__main__":
    clear_screen()
    print("Main Menu")
    print("1.  Get weather by zip code")
    print("2.  Get weather by city, state, and country")
    selection = input("Enter 1 or 2: ")

    match selection:
        case "1":
            print()
            zip = input("Enter a valid zip code: ")
            resp = OpenWeatherMap.GetWeatherByZip(zip)
            if resp["cod"] == 200:
                DisplayResponse(resp)
            else:
                print(f"Error: ({resp["cod"]}) {resp["message"]}")

        case "2":
            print()
            city = input("Enter city name: ")
            state = input("Enter state code: ")
            country = input("Enter country code: ")
            resp = OpenWeatherMap.GetWeatherByCityStateCountry(city, state, country)
            if resp["cod"] == 200:
                DisplayResponse(resp)
            else:
                print(f"Error: ({resp["cod"]}) {resp["message"]}")
        case _:
            print("You must enter 1 or 2")
