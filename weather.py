import json, requests

api_key = "YOUR_API_KEY" # api key is not for disclosing so mentioned YOUR_API_KEY you can log in and use your own api key to make it work.

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
