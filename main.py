from config import CITIES
from extract import todaysWeather

for i in CITIES:
    print(i)
    city = i['city']
    countryCode = i['countryCode']
    print(todaysWeather(city,countryCode))