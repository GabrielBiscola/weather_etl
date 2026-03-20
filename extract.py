import requests

def findGeo(city, countryCode):
    codeURL = (f"https://geocoding-api.open-meteo.com/v1/search")
    params = {
        'name': f'{city}',
        'count': 1,
        'countryCode': {countryCode}
    }
    infoKeys = ['name', 'latitude', 'longitude', 'country', 'admin1']
    response = requests.get(codeURL, params=params)
    json = response.json()

    if json.get('results'):
        results = json['results'][0]
        geoInfo = {k: results[k] for k in infoKeys if k in results}

        return geoInfo

def todaysWeather(city, country):
    geoInfo = findGeo(city, country)
    weatherURL = "https://api.open-meteo.com/v1/forecast"
    params = {
        'latitude': geoInfo.get('latitude'),
        'longitude': geoInfo.get('longitude'),
        'hourly': ['temperature_2m','relative_humidity_2m','rain'],
        'forecast_days': 1
    }
    response = requests.get(weatherURL, params=params)
    json = response.json()

    return json