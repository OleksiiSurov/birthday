import re
import datetime




days = {
    'Today': [],
    'Last weekend': [],
    'Monday': [],
    'Tuesday': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': [],
    'Saturday': [],
    'Sunday': []
}

users = [
    {'name': 'Alex',
     'birthday': datetime.date(1988, 9, 15)},
    {'name': 'Elina',
     'birthday': datetime.date(2015, 9, 16)},
    {'name': 'Juli',
     'birthday': datetime.date(1990, 9, 17)},
    {'name': 'Serge',
     'birthday': datetime.date(1988, 9, 18)},
    {'name': 'Bill',
     'birthday': datetime.date(2015, 9, 19)},
    {'name': 'Tessa',
     'birthday': datetime.date(1990, 9, 20)},
    {'name': 'John',
     'birthday': datetime.date(2015, 9, 21)},
    {'name': 'Anna',
     'birthday': datetime.date(1990, 9, 22)},
    {'name': 'asdasdas',
     'birthday': datetime.date(2015, 9, 14)},
    {'name': 'qweqwewqeqwewq',
     'birthday': datetime.date(1990, 9, 13)}
]

DAY_TODAY = datetime.date.today().strftime("%A")


def result(n: int):
    if len(days['Today']) > 0:
        print(f"{'Today'}: {', '.join(days['Today'])}")
    if DAY_TODAY == 'Monday':
        if len(days['Last weekend']) > 0:
            print(f"{'Last weekend'}: {', '.join(days['Last weekend'])}")

    while True:
        day = datetime.datetime.now() + datetime.timedelta(days=n)
        day_of_week = day.strftime("%A")

        if len(days[day_of_week]) > 0:
            print(f"{day_of_week}: {', '.join(days[day_of_week])}")
        if n == 7:
            break
        n += 1
    return print('Гарного дня!')


def get_birthdays_per_week(users: list):

    """Фнкція отримує на вхід список словників 'users' у форматі ({'name': 'Alex',
     'birthday': datetime.date(2022, 01, 22)})  і виводить
      список користувачів, яких потрібно привітати з днем народження по днях на тиждень вперед"""

    for di in users:
        # різниця днів між поточною датою та днем народження
        timedelta = di['birthday'].replace(year=2022) - datetime.date.today()

        if DAY_TODAY == 'Monday':
            # сінусові значення дня якщо сьогодні понеділок
            try:
                day_before_birth = re.search(r'^-[1,2]\b', str(timedelta)).group()
                days['Last weekend'].append(di.get('name'))
                continue
            except AttributeError:
                pass

        try:
            # кількість днів до дня народження
            day_before_birth = re.search(r'^\d', str(timedelta)).group()

        except AttributeError:
            continue
        if 0 < int(day_before_birth) <= 7:
            # день тижня коли день народження
            day_of_week = di['birthday'].replace(year=2022).strftime("%A")
            days[day_of_week].append(di.get('name'))
        elif int(day_before_birth) == 0:
            days['Today'].append(di.get('name'))


    # виводимо на екран список
    result(0)


get_birthdays_per_week(users)
