import requests
from bs4 import BeautifulSoup

from wzarp.CityWeather import WeatherOfCity

text = "Moscow"
moscow_weather = WeatherOfCity(text)
temp_in_moscow = moscow_weather.get_temp_in_celsius()

def _get_temperature_from_moscow():
    link = "https://www.wunderground.com/weather/ru/{}/".format("Moscow")
    r = requests.get(link)

    page = r.text

    soup = BeautifulSoup(page, "html.parser")
    wclass = "wu-value wu-value-to"
    temp_span = soup.find("span", {"class": wclass})

    temp_in_fahrenheit = int(temp_span.text)
    temp_in_celsius = int(5 / 9 * (temp_in_fahrenheit - 32))
    return temp_in_celsius

assert temp_in_moscow == _get_temperature_from_moscow(),"Something is wrong!"

print("Tests completed successfully")