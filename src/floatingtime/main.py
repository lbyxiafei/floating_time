import schedule
import sys
import time

from datetime import datetime, timedelta
from floatingtime.time_window import TimeWindow


def _show(close_delay=10000):
    tw = TimeWindow(close_delay)
    tw.show()


def _calculate_ts_delta():
    now = datetime.now()
    next_hour = (
        now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    ).replace(second=0)
    delta_00 = (next_hour - now).total_seconds()
    delta_30 = (now.replace(minute=30, second=0, microsecond=0) - now).total_seconds()

    if 0 <= delta_00 < 10:
        return int(delta_00)
    elif 0 <= delta_30 < 10:
        return int(delta_30)
    else:
        return -1


def run_test(close_delay):
    _show(close_delay)


def run_period():
    t = _calculate_ts_delta()
    if t == -1:
        return
    t += 5
    if t < 10:
        t = 10
    _show(t * 1000)


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
    if len(sys.argv) > 1:
        if sys.argv[1] == "debug":
            run_test(2000)
        elif sys.argv[1] == "period":
            run_period()
    else:
        run()
