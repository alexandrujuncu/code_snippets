#!/usr/bin/env python3

import signal
import sys

from time import sleep
from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler


def signal_handler(signal, frame):
    print('Exiting...')
    sys.exit(0)


def job_a():
    print("JobA start@", datetime.now())
    sleep(60)
    print("JobA stop@", datetime.now())


def job_b():
    print("JobB start@", datetime.now())
    sleep(60)
    print("JobB stop@", datetime.now())


def job_c():
    print("JobC start@", datetime.now())
    sleep(60)
    print("JobC stop@", datetime.now())


def add_jobs(sched):
    print("Starting @", datetime.now())

    # Start frist job 1 second after planning it. Doesn't work with now.
    delta = datetime.now() + timedelta(seconds=1)

    sched.add_job(job_a, "interval", start_date=delta, seconds=10)
    sched.add_job(job_b, "interval", start_date=delta, seconds=20)
    sched.add_job(job_c, "interval", start_date=delta, seconds=40)


def main():
    # Setup termination signal.
    signal.signal(signal.SIGINT, signal_handler)

    sched = BlockingScheduler()

    add_jobs(sched)

    sched.start()


if __name__ == "__main__":
    main()
