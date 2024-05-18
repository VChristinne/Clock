from colorama import Fore
import datetime

def get_current_time():
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M\n")

def set_alarm():
    alarm_type = input(Fore.BLUE + "> Set alarm by (1) Exact date or (2) Days from now: " + Fore.RESET)
    if alarm_type == "1":
        year = int(input("Year: "))
        month = int(input("Month: "))
        day = int(input("Day: "))
        hour = int(input("Hour: "))
        minute = int(input("Minute: "))
        alarm = datetime.datetime(year, month, day, hour, minute)
    elif alarm_type == "2":
        days_from_now = int(input(Fore.BLUE + "> Days from now: " + Fore.RESET))
        hour = int(input("Hour: "))
        minute = int(input("Minute: "))
        current_time = datetime.datetime.now()
        alarm = current_time + datetime.timedelta(days=days_from_now)
        alarm = alarm.replace(hour=hour, minute=minute, second=0, microsecond=0)
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