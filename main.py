import clock_setup

def main():
    print(clock_setup.get_current_time())

    alarm = clock_setup.set_alarm()
    print(alarm)

    while True:
        if clock_setup.check_alarm(alarm):
            print("Alarm!")
            break

if __name__ == '__main__':
    main()