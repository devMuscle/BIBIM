# 라이브러리 참조 : https://github.com/ryanking13/SRT

from SRT import SRT
import time
import requests  

class ReservationInfo:
    def __init__(self, start_station, end_station, date, start_time, duration_hour):
        self.start_station = start_station
        self.end_station = end_station
        self.date = date
        self.start_time = start_time
        self.duration_hour = duration_hour
        self.start_hour = int(start_time[:2])
        self.end_hour = self.start_hour + duration_hour

def send_message(message) :
    api_url = "https://notify-api.line.me/api/notify"

    token = "token value"

    headers = {'Authorization':'Bearer '+token}

    message = {
        "message" : message
    }

    requests.post(api_url, headers= headers , data = message)

send_message("start")

def start_macro() :
    for reservation_info in reservation_infos :
        start_hour = reservation_info.start_hour
        end_hour = reservation_info.end_hour
        
        try :
            trains = srt.search_train(reservation_info.start_station, reservation_info.end_station, reservation_info.date, reservation_info.start_time)
        
            for train in trains :

                hour = int(train.dep_time[:2])
    
                if start_hour <= hour <= end_hour:
                    try:
                        reservation = srt.reserve(train)
                        send_message(reservation)
                    except:
                        continue
        except :
            time.sleep(1)
            continue

        time.sleep(1)

loginId = "id" # 회원번호, 이메일, 전화번호 가능
password = "pw"
srt = SRT(loginId, password)

reservation_infos = [
    # 수서, 동대구, 울산(통도사)
    ReservationInfo(start_station='울산(통도사)', end_station='동대구', date='20241028', start_time='140000', duration_hour=4),
    # ReservationInfo(start_station='수서', end_station='동대구', date='20241024', start_time='190000', duration_hour=1),
    # ReservationInfo(start_station='수서', end_station='동대구', date='20241027', start_time='080000', duration_hour=3),
    ReservationInfo(start_station='동대구', end_station='수서', date='20241027', start_time='170000', duration_hour=3)
]

while(True) :
    start_macro()
             
