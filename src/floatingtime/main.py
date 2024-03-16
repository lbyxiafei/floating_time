import schedule, time, sys


from time_window import TimeWindow


def run_job():
    tw = TimeWindow()
    tw.show()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "debug":
        run_job()
        quit()

    # schedule.every().hour.at("29:55").do(run_job)
    schedule.every().hour.at("59:55").do(run_job)

    while True:
        schedule.run_pending()
        time.sleep(1)
