from flask import Blueprint, render_template, session
from app.services.weather_service import WeatherService
from app.utils.auth_decorator import login_required

weather_bp = Blueprint("weather", __name__)

@weather_bp.route("/weather")
@login_required
def weather_page():

    location = session.get("location")

    if location:
        latitude = location.get("latitude")
        longitude = location.get("longitude")
        city = location.get("city", "Your Area")
    else:
        latitude, longitude = 26.8467, 80.9462
        city = "Lucknow"

    weather_data = WeatherService.get_weather(latitude, longitude)

    return render_template(
        "weather.html",
        weather=weather_data,
        city=city
    )