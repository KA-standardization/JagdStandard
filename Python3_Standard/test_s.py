# -*- coding: utf-8 -*-f
import sys
import datetime
from concurrent import futures

from apscheduler.schedulers.blocking import BlockingScheduler

num = 1


# def j(num, scer):
#     if num == 3:
#         print(num)
#         scer.shutdown(wait=False)
def j(num):
    # global scheduler
    print(id(scheduler))
    if num == 3:
        scheduler.shutdown(wait=False)

def get_current_week():
    global num
    if num != 3:
        num += 1

    monday, sunday = datetime.date.today(), datetime.date.today()
    one_day = datetime.timedelta(days=1)
    while monday.weekday() != 0:
        monday -= one_day
    while sunday.weekday() != 6:
        sunday += one_day
    monday = datetime.datetime.strftime(monday, "%Y-%m-%d")
    sunday = datetime.datetime.strftime(sunday, "%Y-%m-%d")

    with futures.ThreadPoolExecutor(1) as thread:
        # thread.submit(j, num, scheduler)
        thread.submit(j, num)
    # if num == 3:
    #     scheduler.shutdown(wait=False)
    print(monday, '|', num)
    return monday


if __name__ == '__main__':
    import time
    scheduler = BlockingScheduler(timezone='Asia/Shanghai')
    print(id(scheduler))
    try:
        scheduler.add_job(get_current_week, 'interval', seconds=2)
        scheduler.start()
    except:
        pass
    time.sleep(0.1)
    print('结束')
