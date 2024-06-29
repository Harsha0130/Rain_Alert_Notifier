import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "--key--"
account_sid = "--sid-id--"
auth_token = "--auth-token--"

weather_params = {
    "lat": 19.075983,
    "lon": 72.877655,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+--sandbox_number--',
        body="Remember to bring an umbrella☔, It's going to be rain today",
        to='whatsapp:+91--ur_number--',
    )
    print(message.status)
