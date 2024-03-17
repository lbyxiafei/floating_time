import schedule
import sys
import time

from floatingtime.time_window import TimeWindow


def _show():
    tw = TimeWindow()
    tw.show()


def run_test():
    _show()


def run():
    # schedule.every().minute.at(":55").do(_show)
    schedule.every().hour.at("29:55").do(_show)
    schedule.every().hour.at("59:55").do(_show)

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "debug":
        run_test()
    else:
        run()
