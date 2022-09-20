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

    """Фнкція отримує на вхід список словників 'users' у форматі ({'name': str,
     'birthday': datetime.date(YYYY, MM, DD)})  і виводить
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
    return result(0)

