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
    print(now,"crawler data update task is activated：")
    if search_web_page():
        print("data is updated！！")
    else:
        print("data is not updated")


# start timed task
def start_schedule():
    print("start timer job:")
    name = "longsongpong"
    # update the data every 12 hours
    schedule.every(720).minutes.do(job, name)
    #schedule.every(1).minutes.do(job, name)
    while True:
        schedule.run_pending()
        time.sleep(1)

# # test interface
# @app.route("/")
# def hellow():
#     return "Hello world"

# acquire information interface
@app.route("/")
@app.route("/index")
@app.route("/infos")
def infos():
    # acquire data information, real-time data crawling from babson college covid website
    days_7,since_aug = get_infos()
    # acquire data from the covid dashboard
    infos = get_table()
    columns= ['city','Total tests last 14 days','Total positive tests last 14 days','rate_percetage','test_total','positive_total',"Positive Rate per 100,000"]
    return render_template("infos.html",days_7 = days_7,since_aug = since_aug,infos=infos,columns=columns)


if __name__ == '__main__':
    t1 = threading.Thread(target=start_schedule,args=())
    t1.setDaemon(True)
    t1.start()

    print("start web")
    app.run(debug=True)
