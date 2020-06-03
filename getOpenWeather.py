#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

APPID = '621882b906accde1a0accf8ed59b6e4e'

import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url ='http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s' % (location,APPID)
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
# print(response.text)

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['weather']
print('Current weather in %s:' % (location))
print(w[0]['main'], '-', w[0]['description'])
