from _datetime import datetime
from random import randint


def get_days_from_today(date):
    date = datetime.strptime(date, "%Y-%m-%d")
    days = (date - datetime.today()).days
    return days


print(abs(get_days_from_today('2020-10-09')))


def get_numbers_ticket(min, max, quantity):
    nums = set()
    while len(nums) < quantity:
        num = randint(min, max)
        nums.add(num)

    return list(nums)


print("Ваші лотерейні числа: " + str(get_numbers_ticket(1, 49, 6)))

