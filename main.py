import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    if not city:
        city = "London"

    api_key = ""  # Replace with your key from OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            result = f"City: {city}\nTemperature: {temperature}°C\nWeather: {description}\nHumidity: {humidity}%\nWind Speed: {wind} m/s"
        else:
            result = f"City '{city}' not found!"
    except:
        result = "Error retrieving data."

    result_label.config(text=result)

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x300")

tk.Label(root, text="Enter City Name:").pack(pady=10)
city_entry = tk.Entry(root, width=25)
city_entry.insert(0, "London")
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 10), justify="left")
result_label.pack(pady=20)

root.mainloop()
