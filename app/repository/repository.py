import requests
from os import environ


def getWeather(city):

    if not city:
        return {
            "error":404
        }

    params = {
        "q": city,
        "appid": environ.get("OPEN_WEATHER_API")
    }
    res = requests.get(
        "https://samples.openweathermap.org/data/2.5/weather", params=params).json()

    name = res["name"]
    main = res["weather"][0]["main"]
    description = res["weather"][0]["description"]
    tempreature = res["main"]["temp"]
    status = 200
    return {

        "data": {
            "city": name,
            "weather": {
                "main": main,
                "description": description,
                "tempreature": tempreature,
            },
        },

        "status": status
    }
