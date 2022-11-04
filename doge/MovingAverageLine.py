import pyupbit
import time
from datetime import date

NowCoin = "KRW-DOGE"

Coin = pyupbit.get_ohlcv(NowCoin)
Close = Coin['close']

today = date.today()

ma60 = Close.rolling(60).mean()
print(ma60)

ma20 = Close.rolling(20).mean()
print(ma20)

buy = False

while True:
    try:
       now_price = pyupbit.get_current_price(NowCoin)

       if buy :
        if now_price <= ma20[today.isoformat()+" 09:00:00"] :            
         print("파세요.")
         buy = False

       else :
        if now_price >= ma60[today.isoformat()+" 09:00:00"] :
         print("매수하세요.")  
         buy = True 

       time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)


