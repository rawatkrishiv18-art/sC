import random
import time

def getrandomdate(start_date, end_date):
    print("random date between", start_date, "and", end_date)
    randomgenerater = random.random()
    dateformat = '%m/%d/%Y'

    start_time = time.mktime(time.strptime(start_date, dateformat))
    end_time = time.mktime(time.strptime(end_date, dateformat))

    random_time = start_time + randomgenerater * (end_time - start_time)
    random_date = time.strftime(dateformat, time.localtime(random_time))
    return random_date

print("random_date:", getrandomdate("1/1/2020", "12/31/2023"))