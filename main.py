import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "7a941c35c1609e319e27bd456ccf9cf0"

weather_params = {
    "lat": 12.971599,
    "lon": 77.594566,
    "apiid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
# print(response.status_code)
print(response.json())

