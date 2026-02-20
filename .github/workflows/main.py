import requests, os
from twilio.rest import Client


OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)
api_key = os.environ.get("OWN_API_KEY")
lat = 48.464718
lon = 35.046185

parameters = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url = OWN_Endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body = "It's going to rain today. Remember to bring an umbrella",
        to='whatsapp:+380979683529'
    )

print(message.status)
