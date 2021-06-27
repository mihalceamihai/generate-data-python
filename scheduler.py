import schedule
import time

def job():
    print("Reading time...")

def coding():
    print("Coding time...")

schedule.every(10).seconds.do(job)
schedule.every(5).seconds.do(coding)

while True:
	schedule.run_pending()

