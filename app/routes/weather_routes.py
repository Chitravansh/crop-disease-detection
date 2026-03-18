from flask import Blueprint, render_template
from app.services.weather_service import WeatherService
from app.utils.auth_decorator import login_required

weather_bp = Blueprint("weather", __name__)


@weather_bp.route("/weather")
@login_required
def weather_page():

    weather_data = WeatherService.get_weather()

    return render_template(
        "weather.html",
        weather=weather_data
    )