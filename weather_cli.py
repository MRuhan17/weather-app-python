import requests

API_KEY = "4f8793af4494312992e098e4dd859f3e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"  # Celsius
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            city_name = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"].capitalize()

            print(f"\n🌍 Weather in {city_name}, {country}:")
            print(f"🌡 Temperature: {temp}°C")
            print(f"💧 Humidity: {humidity}%")
            print(f"☁ Condition: {condition}")
        else:
            print(f"❌ Error: {data['message'].capitalize()}")

    except Exception as e:
        print("⚠ Something went wrong:", e)


if __name__ == "__main__":
    print("=== 🌦 Weather App CLI ===")
    city = input("Enter city name: ")
    get_weather(city)
