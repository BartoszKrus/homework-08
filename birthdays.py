from datetime import datetime, timedelta
from collections import defaultdict


def is_leap(year):
    '''
    Function checks if the year is leap year
    '''
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def update_birthdays(users):
    '''
    The function changes birthdays to the future date of the birthday celebration.
    Function logic:
    - if the year is not leap year, change 29.02 to 28.02 (change for the case of a person who was born on February 29),
    - if more than 30 days have passed since the user's birthday, set the year to the next year (notation needed for the case of the last week of the year),
    - if the birthday falls on Saturday or Sunday, move it to Monday
    '''
    current_year = datetime.now().year
    current_date = datetime.now().date()

    for user in users:
        birthday = user["birthday"]

        if birthday.month == 2 and birthday.day == 29 and not is_leap(current_year):
            user["birthday"] = user["birthday"].replace(year=current_year, day=28)
        else:
            user["birthday"] = user["birthday"].replace(year=current_year)

        if current_date > user["birthday"].date() + timedelta(days=30):
            user["birthday"] = user["birthday"].replace(year=current_year + 1)

        if user["birthday"].weekday() == 5:
            user["birthday"] += timedelta(days=2)
        elif user["birthday"].weekday() == 6:
            user["birthday"] += timedelta(days=1)

    return users


def get_birthdays_per_week(users):
    '''
    The function displays a list of people along with the day of the week when you need to make a wish next week
    '''
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    birthdays = defaultdict(list)    
    today = datetime.now().date()
    next_monday = today + timedelta(days=(7 - today.weekday() or 7))
    next_week = [next_monday + timedelta(days=i) for i in range(7)]

    for user in users:
        if user["birthday"].date() in next_week:
            day_of_week = days_of_week[user["birthday"].weekday()]
            birthdays[day_of_week].append(user["name"])

    print(f"People celebrating birthdays next week:")
    for day_of_week in days_of_week:
        if birthdays[day_of_week]:
            print(f"{day_of_week}: {', '.join(birthdays[day_of_week])}")


if __name__ == "__main__":
    users = [
        {"name": "Darek", "birthday": datetime(1986, 1, 5)},
        {"name": "Agnieszka", "birthday": datetime(1986, 1, 6)},
        {"name": "Marcelina", "birthday": datetime(1980, 1, 7)},
        {"name": "Lila", "birthday": datetime(1970, 1, 8)},
        {"name": "Pola", "birthday": datetime(1995, 1, 12)},
        {"name": "Monika", "birthday": datetime(1995, 1, 13)},
        {"name": "Mariusz", "birthday": datetime(1980, 1, 14)},
        {"name": "Tomek", "birthday": datetime(1970, 1, 15)},
        {"name": "Bartek", "birthday": datetime(1995, 1, 19)},
        {"name": "Michał", "birthday": datetime(1991, 1, 20)},
        {"name": "Damian", "birthday": datetime(1991, 1, 21)},
        {"name": "Rafał", "birthday": datetime(2000, 2, 29)},
        {"name": "Filip", "birthday": datetime(2003, 1, 10)},
        {"name": "Łukasz", "birthday": datetime(2003, 1, 2)},
        {"name": "Wojtek", "birthday": datetime(2003, 12, 28)}
    ]
    # help(is_leap)
    # help(update_birthdays)
    # help(get_birthdays_per_week)
    new_year_users = update_birthdays(users)
    get_birthdays_per_week(new_year_users)



