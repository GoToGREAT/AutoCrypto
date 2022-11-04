import pyupbit
import time
from datetime import date

NowCoin = "KRW-DOGE"

Coin = pyupbit.get_ohlcv(NowCoin)
Close = Coin['close']

ma60 = Close.rolling(60).mean()
print(ma60)

ma20 = Close.rolling(20).mean()
print(ma20)

print(Close)

print(Close[0])

buy = False

haveMoney = 100
haveCoin = 0

for i in range(5, 199):  

    if buy :
        if Close[i] <= ma20[i] :            
         haveMoney = haveCoin*Close[i]
         haveCoin = 0 
         buy = False

    else :
        if Close[i] >= ma60[i] :
         haveCoin = Close[i]/haveMoney
         haveMoney = 0          
         buy = True  

print("계산이 끝났습니다.")
if buy :
    print(haveCoin*Close[199])
else :
    print(haveMoney)