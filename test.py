import pyupbit

access = "0H2budxcT0TBjWW0Bjsq6SseVEji5Uw7ixIWhgZ7"          # 본인 값으로 변경
secret = "8Kxs3LYkRJfGX9tdAjePxrwdN3ot2G2xS6V41h2x"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회


