import pyupbit
import time
from datetime import date
import requests

NowCoin = "KRW-DOGE"

Coin = pyupbit.get_ohlcv(NowCoin)
Close = Coin['close']

today = date.today()

ma60 = Close.rolling(60).mean()
print(ma60)

ma20 = Close.rolling(20).mean()
print(ma20)

buy = False

token = "xoxb-4296737263574-4320693496581-hCRlm9L6p9kyyxDtnzVG2i1p"
channel = "#doge_upbit"


while True:
    try:
       now_price = pyupbit.get_current_price(NowCoin)

       if buy :
        if now_price <= ma20[today.isoformat()+" 09:00:00"] :            
         print("파세요.")
         text = "판매 합니다."
         requests.post("https://slack.com/api/chat.postMessage",
         headers={"Authorization": "Bearer "+token},
         data={"channel": channel,"text": text})
         buy = False

       else :
        if now_price >= ma60[today.isoformat()+" 09:00:00"] :
         print("매수하세요.")
         text = "매수 합니다."
         requests.post("https://slack.com/api/chat.postMessage",
         headers={"Authorization": "Bearer "+token},
         data={"channel": channel,"text": text})  
         buy = True 

       time.sleep(1)
    except Exception as e:
        print(e)
        text = "오류가 발생했습니다."+e
        requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text})  
        time.sleep(1)


