import clock_setup
from colorama import Fore

def main():
    clock_setup.get_current_time()

    alarm = clock_setup.set_alarm()
    print(Fore.RED + f"\nAlarm set to: {alarm}" + Fore.RESET)

    while True:
        if clock_setup.check_alarm(alarm):
            print("\nAlarm!")
            break

if __name__ == '__main__':
    main()