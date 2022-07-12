import requests
from datetime import date

API_key = "INSERT API KEY HERE"
base_url = "https://openweathermap.org/"

print("Hello there! This program will display today's date and the weather of the city you're located in!\n")

city = input("Enter your city name: ")
request_url = f"https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid={API_key}"
response = requests.get(request_url)

if response.status_code == 200:
   today = date.today()
   print("Today's date is:", today)

   data = response.json()
   weather = data["weather"][0]['description']
   print("Today's weather is:", weather)

   temperature = round(data["main"]["temp"] - 273.15, 2)
   print("Today's temperature is:", temperature, "celsius")

else:
   print("An error occurred.")
