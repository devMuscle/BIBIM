# bibim 사용법
1. 주석처리된 라이브러리 참조를 확인하여 라이브러리 설치하기
```shell
pip install SRTrain
```
2. 라인에서 알림용 토큰 발급 받기 <br>
https://velog.io/@denver_almighty/%EB%9D%BC%EC%9D%B8-Notify-%EB%B4%87-%EB%A7%8C%EB%93%A4%EA%B8%B0 참조
(현재 예약시 알림이 정상 발송이 안되는 오류 존재, 또한 라인 알림 서비스 만료에 맞춰 마이그레이션 필요)

3. loginId, password 에 본인 로그인 정보 입력하기

4. reservation_info 배열에 예약 정보 추가하기 (ReservationInfo 객체)
   - duration_hour 은 구간 설정 => start_time = '170000', duration_hour = 2 이면 17시 부터 19시 사이를 탐색하는 것

etc.
  time.sleep(1) 로직이 성능을 저하시키지만 없을시 ip밴 될 수 있음
