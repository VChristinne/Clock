from colorama import Fore
import datetime

def get_current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def set_alarm():
    alarm_type = input(Fore.BLUE + "> Set alarm by (1) Exact date or (2) Days from now: " + Fore.RESET)
    if alarm_type == "1":
        alarm_input = input("Enter date and time (dd/mm hh:mm): ")
        date, time = alarm_input.split()
        day, month = date.split('/')
        hour, minute = time.split(':')
        year = datetime.datetime.now().year
        alarm = datetime.datetime(year, int(month), int(day), int(hour), int(minute))
    elif alarm_type == "2":
        days_from_now = int(input(Fore.BLUE + "> Days from now: " + Fore.RESET))
        time = input("Enter time (hh:mm): ")
        hour, minute = time.split(':')
        current_time = datetime.datetime.now()
        alarm = current_time + datetime.timedelta(days=days_from_now)
        alarm = alarm.replace(hour=int(hour), minute=int(minute), second=0, microsecond=0)
    else:
        print("Invalid option. Please choose 1 or 2.")
        return None
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