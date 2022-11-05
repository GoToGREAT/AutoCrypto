import pyupbit

# 업비트 로그인
access = "0H2budxcT0TBjWW0Bjsq6SseVEji5Uw7ixIWhgZ7"
secret = "8Kxs3LYkRJfGX9tdAjePxrwdN3ot2G2xS6V41h2x"

upbit = pyupbit.Upbit(access, secret)

NowCoin = "KRW-DOGE"

print("도지 갯수 : ")
print(upbit.get_balance(NowCoin))   

print("-----------------------------------------")

print("보유현금 : ")
print(upbit.get_balance("KRW"))