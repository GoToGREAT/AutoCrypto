import time
import pyupbit
import datetime

access = "0H2budxcT0TBjWW0Bjsq6SseVEji5Uw7ixIWhgZ7"
secret = "8Kxs3LYkRJfGX9tdAjePxrwdN3ot2G2xS6V41h2x"

NowCoin = "KRW-DOGE"
val_K = 0.01

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")



# 자동매매 시작
while True:
    try:
       print(pyupbit.get_current_price("KRW-DOGE"))
       print(upbit.get_balance("KRW-DOGE"))     # KRW-Doge 조회
       time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)