from korail2 import *
import time
import requests

def send_message(message) :
    api_url = "https://notify-api.line.me/api/notify"
    token = "token_value"

    headers = {'Authorization':'Bearer '+ token}

    message = {
        "message" : message
    }

    requests.post(api_url, headers= headers , data = message)

class ReservationInfo:
    def __init__(self, dep, arr, date, leave_time):
        self.dep = dep
        self.arr = arr
        self.date = date
        self.leave_time = leave_time

reservation_infos = [
    ReservationInfo(dep='서울', arr='동대구', date='20241101', leave_time='210000')
]

korail = Korail("id", "pw")
answer = korail.login()

# one_psgrs = [AdultPassenger()]
# two_psgrs = [AdultPassenger(2)]

send_message("Welcome To KTX World!")

def start_macro() :
    for reservation_info in reservation_infos :

        try : 
            trains = korail.search_train(reservation_info.dep, reservation_info.arr, reservation_info.date, reservation_info.leave_time)

            for train in trains :
                try :
                    print(train)
                    reservation = korail.reserve(train)
                    send_message(reservation)
                except Exception as e:
                    print(e)
                    time.sleep(1)
                    continue
        except :
            time.sleep(1)
            continue

while(True) :
    start_macro()
