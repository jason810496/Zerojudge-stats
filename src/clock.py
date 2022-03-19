from apscheduler.schedulers.blocking import BlockingScheduler

import requests as req

from ZJquery import ZJ

print("Check Scheduled job")

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='0-6', minute='*/20')
def scheduled_job():
    
    print("Check Heroku alive")
    req.get(url="https://zj-query-0.herokuapp.com/")
    
    print("Maintain connection to ZJ ")
    ZJ.Is_Connect()

sched.start()