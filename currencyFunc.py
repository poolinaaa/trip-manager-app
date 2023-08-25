import csv
from datetime import datetime, timedelta
from time import sleep


def checkingCurrency(country):
    with open('countryCurrency.csv') as csvFile:
        csvRead = csv.reader(csvFile, delimiter=',')
        for row in csvRead:
            if row[0] == country:
                currencyCode = row[3]
        if 'currencyCode' not in locals():
            return 'CountryError'
        else:
            return currencyCode


def checkingBase(currency):
    with open('countryCurrency.csv') as csvFile:
        csvRead = csv.reader(csvFile, delimiter=',')
        for row in csvRead:
            if row[3] == currency:
                return currency
        if 'result' not in locals():
            print(
                'BaseCurrencyError: correct base currency name, current base is set default (EUR)')
            return 'EUR'


def decorator1(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        sleep(1)
        end = datetime.now()
        runTime = end - start
        return runTime-timedelta(seconds=1)
    return wrapper
