import pyupbit
import time
from datetime import date
import requests

NowCoin = "KRW-DOGE"

Coin = pyupbit.get_ohlcv(NowCoin)
Close = Coin['close']

ma60 = Close.rolling(60).mean()
# print(ma60)

ma20 = Close.rolling(20).mean()
# print(ma20)

# print(Close)

# print(Close[0])

buy = False

haveMoney = 100
haveCoin = 0

# 수수료 무시
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

print("수수료 무시 : 계산이 끝났습니다.")
if buy :
    print(haveCoin*Close[199])
else :
    print(haveMoney)


# 슬랙 로그인
token = "xoxb-4296737263574-4320693496581-hCRlm9L6p9kyyxDtnzVG2i1p"
channel = "#doge_upbit"

def SendMessage(text):
    requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": text})


# 수수료 포함
buy = False

haveMoney = 100
haveCoin = 0

# 수수료 무시
SendMessage("테스트를 시작합니다.")
for i in range(5, 199):     
    if buy :
        if Close[i] <= ma20[i] :            
         haveMoney = haveCoin*Close[i]*0.9995
         haveCoin = 0
         text = "판매 합니다."
         SendMessage(text)
         SendMessage("판매 기준 가격 : "+str(Close[i]))
         SendMessage("현재 가진 돈 : "+str(haveMoney))
         buy = False

    else :
        if Close[i] >= ma60[i] :
         haveCoin = Close[i]/(haveMoney*0.9995)
         haveMoney = 0
         text = "구매 합니다."
         SendMessage(text)
         SendMessage("구매한 돈 : "+str(Close[i]/(haveMoney*0.9995)))
         SendMessage("구매 기준 가격 : "+str(Close[i]))
         SendMessage("구매 수량 : "+ str(haveCoin))          
         buy = True  

print("수수료 포함 : 계산이 끝났습니다.")
if buy :
    text = "수수료 포함 : 계산이 끝났습니다."
    SendMessage(text)
    finish = (haveCoin*Close[199]*0.9995)
    print(finish)
    SendMessage(finish)
else :
    text = "수수료 포함 : 계산이 끝났습니다."
    SendMessage(text)
    finish = haveMoney
    print(finish)
    SendMessage(finish)



text = "테스트 종료"
SendMessage(text)