from collections import defaultdict
from datetime import datetime, timedelta
import random
from pprint import pprint

# исправить сортировку по дню года

def get_users_w_random_dirthday_list(now_many = 10):
    users_birthdays_list = []
    current_datetime = datetime.now()
    for i in range(1, now_many+1):        
        day_of_year = random.randint(1,365)
        year_of_birth = random.randint(current_datetime.year - 50,current_datetime.year - 18)
        user_birthday = {'name': f'User{i}',
                         'birthday': datetime.strptime(f"{year_of_birth}-{day_of_year}", "%Y-%j").date()}
        users_birthdays_list.append(user_birthday)
    return users_birthdays_list

def get_next_week_start(d: datetime):
    diff_days = 7 - d.weekday()
    return d + timedelta(days = diff_days)

def get_birthdays_per_week(users_birthdays_list):
    congratulationdays_users = defaultdict(list)
    today = datetime.now().date()
    next_week_start = get_next_week_start(today)
    start_period = next_week_start - timedelta(2)
    end_period = next_week_start + timedelta(4)
    print(start_period, end_period)
    user_birthday_thisyear_list = []
    for user_birthday in users_birthdays_list:
        # print(user_birthday['birthday'])
        if user_birthday['birthday'].month == 2 and user_birthday['birthday'].day == 29:
            user_birthday['birthday_thisyear'] = datetime(datetime.now().year, 3, 1).date()
        else:
            user_birthday['birthday_thisyear'] = datetime(datetime.now().year, user_birthday['birthday'].month,user_birthday['birthday'].day).date()
        if user_birthday['birthday_thisyear'] >= start_period and user_birthday['birthday_thisyear'] <= end_period:
            user_birthday_thisyear_list.append(user_birthday)
    print(user_birthday_thisyear_list)
    for user_birthday_thisyear in sorted(user_birthday_thisyear_list, key=lambda d: d['birthday_thisyear'], reverse=True):
        print(user_birthday_thisyear['name'], user_birthday_thisyear['birthday'], user_birthday_thisyear['birthday_thisyear'])
        if user_birthday_thisyear['birthday_thisyear'].weekday() in (5,6):
            congratulationdays_users['Monday'].append(user_birthday_thisyear['name'])
        else:
            congratulationdays_users[user_birthday_thisyear['birthday_thisyear'].strftime('%A')].append(user_birthday_thisyear['name'])
    return congratulationdays_users

if __name__ == '__main__':
    users_birthdays_list = get_users_w_random_dirthday_list(now_many = 500)
    congratulationdays_users = get_birthdays_per_week(users_birthdays_list)
    pprint(congratulationdays_users)

    