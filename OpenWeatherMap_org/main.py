from get_weather import OpenWeatherMap
from datetime import datetime

def DisplayResponse(resp):
    if resp["cod"] == 200:
        city_name = resp["name"]
        weather = resp["weather"][0]["main"]
        temp = resp["main"]["temp"]
        feels_like = resp["main"]["feels_like"]

        rise_time = resp["sys"]["sunrise"]
        set_time = resp["sys"]["sunset"]
        sunrise = datetime.fromtimestamp(rise_time)
        sunset = datetime.fromtimestamp(set_time)

        print()
        print(f"Current weather conditions for {city_name}")
        print(f"{weather}")
        print(f"Temperature: {temp}")
        print(f"Feels Like: {feels_like}")
        print()
        print(f"Sunrise at {sunrise.strftime("%I:%M %p")} local time")
        print(f"Sunset at {sunset.strftime("%I:%M %p")} local time")
        print()
    else:
        print(f"Error: ({resp["cod"]}) {resp["message"]}")

if __name__ == "__main__":
    print("Main Menu")
    print("1.  Get weather by zip code")
    print("2.  Get weather by city, state, and country")
    selection = input("Enter 1 or 2: ")

    match selection:
        case "1":
            print()
            zip = input("Enter a valid zip code: ")
            resp = OpenWeatherMap.GetWeatherByZip(zip)
            DisplayResponse(resp)
        case "2":
            print()
            city = input("Enter city name: ")
            state = input("Enter state code: ")
            country = input("Enter country code: ")
            resp = OpenWeatherMap.GetWeatherByCityStateCountry(city, state, country)
            DisplayResponse(resp)
        case _:
            print("You must enter 1 or 2")
