import sqlite3 as sql
import json
import pprint
import requests
from numpy import sin, cos, arccos, pi, round


def rad2deg(radians):
    degrees = float(radians) * 180 / pi
    return degrees


def deg2rad(degrees):
    radians = float(degrees) * pi / 180
    return radians


def getDistanceBetweenPoints(latitude1, longitude1, latitude2, longitude2, unit='kilometers'):

    theta = float(longitude1) - float(longitude2)

    distance = 60 * 1.1515 * rad2deg(
        arccos(
            (sin(deg2rad(latitude1)) * sin(deg2rad(latitude2))) +
            (cos(deg2rad(latitude1)) * cos(deg2rad(latitude2)) * cos(deg2rad(theta)))
        )
    )

    if unit == 'miles':
        return round(distance, 2)
    if unit == 'kilometers':
        return round(distance * 1.609344, 2)


def searchAttractions(lng, lat):
    url = 'https://api.geoapify.com/v2/places'

    params = dict(categories='tourism.attraction',
                  filter=f'circle:{lng},{lat},5000', limit=10, apiKey='f17cce1b808a4e39845aca4cf631bf04')

    resp = requests.get(url=url, params=params)

    try:
        data = resp.json()
    except json.JSONDecodeError:
        print('wrong format of data')
    else:
        return (data)


def createTable(nameOfDb, nameOfTable):
    con = sql.connect(f'{nameOfDb}.db')
    cur = con.cursor()
    cur.execute(f'''CREATE TABLE if not exists {nameOfTable} (
                attractionId INTEGER,
                nameOfAttraction TEXT,
                address TEXT,
                wantToSee TEXT,
                PRIMARY KEY (attractionId))''')
    con.commit()
    cur.close()


pprint.pprint(searchAttractions(17, 51))
