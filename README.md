# Rain Alert Notifier
- This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp for 2023" course by Dr. Angela Yu.

### Weather Notification Script Overview

- **Purpose:**
  - Developed a Python script to provide weather notifications based on forecast data from OpenWeatherMap API and send alerts via Twilio's WhatsApp API when rain is expected.

- **API Integration:**
  - Integrated the OpenWeatherMap API (`api.openweathermap.org`) to fetch weather forecast data by specifying latitude (`lat`) and longitude (`lon`) coordinates.

- **Weather Condition Check:**
  - Implemented a check within the script to iterate through forecasted weather data (`weather_data["list"]`) and determine if any condition codes (`"weather"[0]["id"]`) indicate potential rain (conditions with code < 700).

- **Twilio Integration:**
  - Utilized Twilio's REST API (`twilio.rest.Client`) to facilitate sending WhatsApp messages (`client.messages.create`) to notify users about impending rain conditions.

- **Title and Description:**
  - Clearly stated the purpose of the script and its functionality.

- **Prerequisites:**
  - Listed the necessary prerequisites such as Python installation and required Python libraries (`requests`, `twilio`).

###Replace placeholders in the script:

- Replace `--key--` with your OpenWeatherMap API key.
- Replace `--sid-id--` with your Twilio Account SID.
- Replace `--auth-token--` with your Twilio Auth Token.
- Replace `--sandbox_number--` with your Twilio WhatsApp sandbox number.
- Replace `--ur_number--` with your WhatsApp number.


###Screenshot

![WhatsApp Image 2024-06-29 at 19 48 27_69934f14](https://github.com/Harsha0130/Rain_Alert_Notifier/assets/127675058/b404a134-158f-409c-ace4-6825c4e35547)



