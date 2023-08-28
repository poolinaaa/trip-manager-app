import csv

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


