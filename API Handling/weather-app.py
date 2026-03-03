import requests

def get_coordinates(city):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    response = requests.get(geo_url)

    if response.status_code == 200:
        data = response.json()
        if "results" in data:
            lat = data["results"][0]["latitude"]
            lon = data["results"][0]["longitude"]
            return lat, lon
        else:
            return None, None
    else:
        return None, None


def get_weather(lat, lon):
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(weather_url)

    if response.status_code == 200:
        data = response.json()
        return data["current_weather"]["temperature"]
    else:
        return None


def main():
    city = input("Enter city name: ")

    lat, lon = get_coordinates(city)

    if lat is None:
        print("City not found.")
        return

    temperature = get_weather(lat, lon)

    if temperature is not None:
        print(f"Current temperature in {city}: {temperature}°C")
    else:
        print("Could not fetch weather data.")


if __name__ == "__main__":
    main()