import time
import schedule
import sys

from floatingtime.time_window import TimeWindow


def _show():
    tw = TimeWindow()
    tw.show()


def debug():
    _show()


def run():
    # schedule.every().minute.at(":55").do(_show)
    schedule.every().hour.at("29:55").do(_show)
    schedule.every().hour.at("59:55").do(_show)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "debug":
        debug()
    else:
        run()
