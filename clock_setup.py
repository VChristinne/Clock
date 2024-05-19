from colorama import Fore
import datetime
from time import sleep

def get_current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def set_alarm():
    alarm_input = input(Fore.BLUE + "> Set alarm (dd/mm hh:mm): " + Fore.RESET)
    date, time = alarm_input.split()
    day, month = date.split('/')
    hour, minute = time.split(':')
    year = datetime.datetime.now().year
    alarm = datetime.datetime(year, int(month), int(day), int(hour), int(minute))
    return alarm

def check_alarm(alarm):
    current_time = datetime.datetime.now()
    if current_time == alarm:
        return True
    else:
        return False

def time_remaining(alarm):
    current_time_str = get_current_time()
    current_time = datetime.datetime.strptime(current_time_str, "%H:%M:%S")
    current_time = datetime.datetime.combine(datetime.date.today(), current_time.time())
    remaining_time = alarm - current_time

    if remaining_time.total_seconds() <= 0:
        check_alarm(alarm)
        print(Fore.RED + "\nAlarm!" + Fore.RESET)
        exit()

    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"