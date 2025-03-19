from get_weather import OpenWeatherMap

def DisplayResponse(resp):
    if resp["cod"] == 200:
        weather = resp["weather"][0]["main"]
        temp = resp["main"]["temp"]
        feels_like = resp["main"]["feels_like"]

        print()
        print(f"Current weather conditions for zip code {zip}")
        print(f"{weather}")
        print(f"Temperature: {temp}")
        print(f"Feels Like: {feels_like}")
        print()
    else:
        print(f"Error: ({resp["cod"]}) {resp["message"]}")

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
