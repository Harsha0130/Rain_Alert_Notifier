import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "7a941c35c1609e319e27bd456ccf9cf0"

weather_params = {
    "lat": 12.971599,
    "lon": 77.594566,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Carry Umbrella")

