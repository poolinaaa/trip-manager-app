from datetime import datetime, timedelta
from time import sleep

def decorator1(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        sleep(1)
        end = datetime.now()
        runTime = end - start
        return runTime-timedelta(seconds=1)
    return wrapper