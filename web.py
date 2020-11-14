from flask import Flask,render_template
from service import *
import schedule
import threading
import time
import datetime
from crawler import *

app = Flask(__name__)

# timed task
def job(name):
    now = datetime.datetime.now()
    print(now,"crawler data update task is activated:")
    if search_web_page():
        print("data is updated！")
    else:
        print("data is not updated")

# start timed task
def start_schedule():
    print("start timer job:")
    name = "longsongpong"
    # update the data every 20 seconds
    schedule.every(20).seconds.do(job, name)
    #schedule.every(1).minutes.do(job, name)
    while True:
        schedule.run_pending()
        time.sleep(1)

# test interface
@app.route("/")
def hellow():
    return "Hello world"