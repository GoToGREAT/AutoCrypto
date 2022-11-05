import pyupbit
import time
from datetime import date
import requests

# 업비트 로그인
access = "0H2budxcT0TBjWW0Bjsq6SseVEji5Uw7ixIWhgZ7"
secret = "8Kxs3LYkRJfGX9tdAjePxrwdN3ot2G2xS6V41h2x"

upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 슬랙 로그인
token = "xoxb-4296737263574-4320693496581-hCRlm9L6p9kyyxDtnzVG2i1p"
channel = "#doge_upbit"

def SendMessage(text):
    requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": text})


NowCoin = "KRW-DOGE"

Coin = pyupbit.get_ohlcv(NowCoin)
Close = Coin['close']

today = date.today()

ma60 = Close.rolling(60).mean()
print(ma60)
print(ma60[-1])
ma20 = Close.rolling(20).mean()
print(ma20)
print(ma20[-1])

buy = False



while True:
    try:
       now_price = pyupbit.get_current_price(NowCoin)

       if buy :
        if now_price <= ma20[today.isoformat()+" 09:00:00"] :            
         print("파세요.")
         SendMessage("판매 합니다.")
         buy = False

       else :
        if now_price >= ma60[today.isoformat()+" 09:00:00"] :
         print("매수하세요.")
         SendMessage("매수 합니다.") 
         buy = True 

       time.sleep(1)
    except Exception as e:
        print(e)
        SendMessage("오류 발생")
        SendMessage(str(e)) 
        time.sleep(1)