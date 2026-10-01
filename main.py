temp=input("請輸入溫度: ")
temp=int(temp)

if temp >= 35:
    print("過熱")
elif temp > 20:
    print("偏高")
else:
    print("正常")