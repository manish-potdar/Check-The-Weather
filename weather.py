import json, requests

api_key = "2745389ebc1daa517aa5ff62c363f580"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()


if x['cod'] != "404":
    y = x["main"]
    current_temperature = y['temp']
    current_pressure = y['pressure']
    current_humidity = y['humidity']
    z = x["weather"]

    weather_description = z[0]["description"]

    print(" Temperature (in Celcius unit) = " +
                str(current_temperature - 273.15) +
            "\n atmospheric pressure (in hPa unit) = " +
                str(current_pressure) +
            "\n humidity (in percentage) = " +
                str(current_humidity) +
            "\n description = " +
                str(weather_description) + 
            "\n Have a Nice Day!" )

else:
    print(" City Not Found ")
