from datetime import datetime

def get_birthdays_per_week(users):
    today = datetime.today().date()
    # Debug
    # today = today.replace(day=today.day + 4)
    # print(today)
    ret = {}
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            delta_days = birthday_this_year.weekday()
            if not delta_days in ret:
                ret[delta_days] = []
            ret[delta_days].append(name)
    buff = []
    for day_index_from_today in range(today.weekday(), today.weekday() + 7):
        index = day_index_from_today % 7
        if index in ret:
            if index == 0:
                buff.extend(ret[index])
                if len(buff) > 0:
                    print(f'{week_days[index]}: {", ".join(buff)}')
                buff.clear()
            elif index < 5:
                print(f'{week_days[index]}: {", ".join(ret[index])}')
            else:
                buff.extend(ret[index])
    if len(buff) > 0:
        print(f'{week_days[0]}: {", ".join(buff)}')

if __name__ == "__main__":
    users_data = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
        {"name": "Alexander Kukla", "birthday": datetime(1986, 3, 19)},
        {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
        {"name": "Stephen Gary Wozniak", "birthday": datetime(1950, 8, 11)},
        {"name": "Linus Benedict Torvalds", "birthday": datetime(1969, 12, 28)},
        {"name": "20 Friday user 1", "birthday": datetime(1969, 10, 20)}, # Friday
        {"name": "14 Saturday user 2", "birthday": datetime(1975, 10, 14)}, # Saturday
        {"name": "16 Monday user 3", "birthday": datetime(1943, 10, 16)}, # Monday
        {"name": "15 Sunday user 4", "birthday": datetime(1969, 10, 15)}, # Sunday
        {"name": "19 Thursday user 5", "birthday": datetime(1969, 10, 19)}, # Thursday
        {"name": "22 Sunday user 6", "birthday": datetime(1969, 10, 22)}, # Sunday
        {"name": "18 Wednesday user 7", "birthday": datetime(1969, 10, 18)}, # Wednesday
        {"name": "23 Monday user 8", "birthday": datetime(1969, 10, 23)}, # Monday
        {"name": "24 Tuesday user 9", "birthday": datetime(1969, 10, 24)}, # Tuesday
    ]

    get_birthdays_per_week(users_data)
