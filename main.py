import clock_setup
from colorama import Fore
from time import sleep

def main():
    alarm = clock_setup.set_alarm()
    if alarm is None:
        print("Invalid alarm setting. Please restart the program and choose a valid option.")
        return

    print(Fore.RED + "\nAlarm set to: " + Fore.RESET + f"{alarm}")

    while True:
        current_time = clock_setup.get_current_time()
        remaining_time = clock_setup.time_remaining(alarm)

        print(Fore.GREEN + "\rCurrent time: " + Fore.RESET + f"{current_time} | " + Fore.BLUE + "Time remaining: " + Fore.RESET + f"{remaining_time}", end="", flush=True)
        sleep(1)

if __name__ == '__main__':
    main()