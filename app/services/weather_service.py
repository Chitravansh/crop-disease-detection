import requests


class WeatherService:

    @staticmethod
    def get_weather(latitude=26.8467, longitude=80.9462):

        url = "https://api.open-meteo.com/v1/forecast"

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True,
            "hourly": [
                "relativehumidity_2m",
                "precipitation_probability",
                "windspeed_10m"
            ],
            "daily": [
                "temperature_2m_max",
                "temperature_2m_min",
                "precipitation_probability_max"
            ],
            "timezone": "auto"
        }

        try:
            response = requests.get(url, params=params, timeout=5)
            data = response.json()

            current = data["current_weather"]

            weather_data = {
                "temperature": current["temperature"],
                "wind": current["windspeed"],
                "weather_code": current["weathercode"],
                "forecast": [],
                "humidity": data["hourly"]["relativehumidity_2m"][0],
                "rain_probability": data["hourly"]["precipitation_probability"][0],
            }

            for i in range(7):
                weather_data["forecast"].append({
                    "date": data["daily"]["time"][i],
                    "temp_max": data["daily"]["temperature_2m_max"][i],
                    "temp_min": data["daily"]["temperature_2m_min"][i],
                    "rain": data["daily"]["precipitation_probability_max"][i]
                })

            return weather_data

        except Exception as e:
            print("Weather API Error:", str(e))

            return {
                "temperature": "N/A",
                "wind": "N/A",
                "weather_code": 0,
                "humidity": "N/A",
                "rain_probability": "N/A",
                "forecast": []
            }