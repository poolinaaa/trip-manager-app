import requests
import json
import config as c
from datetime import timedelta
import csv


def searchCoordinates():
    country = c.countryName.get().capitalize()
    with open('worldcities.csv', encoding='utf8') as csvFile:
        csvRead = csv.reader(csvFile, delimiter=',')
        for row in csvRead:
            if row[4] == country:
                if row[8] == 'primary':
                    lat = row[2]
                    lng = row[3]
                    break
    return lat, lng


def getWeather():
    lat, lng = searchCoordinates()
    date = c.dateFlight
    yearAgo = date - timedelta(days=365)
    yearAgoPlusMonth = yearAgo + timedelta(days=30)

    paramsArchive = {'latitude': lat,
                     'longitude': lng,
                     'start_date': yearAgo,
                     'end_date': yearAgoPlusMonth,
                     'daily': 'temperature_2m_mean',
                     'timezone': 'GMT'}
    
    paramsCurrent = {'latitude':lat,
                     'longitude':lng,
                     'hourly':'temperature_2m,precipitation_probability,precipitation'}

    urlArchive = 'https://archive-api.open-meteo.com/v1/archive'

    urlCurrent = 'https://api.open-meteo.com/v1/forecast'

    reqArchive = requests.get(url=urlArchive, params=paramsArchive)
    reqCurrent = requests.get(url=urlCurrent, params=paramsCurrent)

    try:
        current = reqCurrent.json()
        print(current)
    except json.JSONDecodeError:
        print('error forecast')
    finally:
        pass

    try:
        archive = reqArchive.json()
        print(archive)
    except json.JSONDecodeError:
        print('error archive weather')
    finally:
        pass
