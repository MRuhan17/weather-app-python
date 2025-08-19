import requests
import tkinter as tk
from tkinter import messagebox

# Replace with your actual API key
API_KEY = "your_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("cod") != 200:
            return None

        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]

        return f"📍 {city_name}, {country}\n🌡 Temp: {temp}°C\n🌤 Weather: {weather}\n💧 Humidity: {humidity}%"

    except Exception as e:
        return None

def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return
    
    weather_info = get_weather(city)
    if weather_info:
        result_label.config(text=weather_info)
    else:
        messagebox.showerror("Error", "City not found or API error!")

# Tkinter UI setup
root = tk.Tk()
root.title("Weather App 🌦")
root.geometry("350x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Weather App", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=show_weather)
search_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

root.mainloop()
