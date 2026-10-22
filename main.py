data=["25.1","壞","26.3","x","24.8"]
e=[]
count=0
total=0
for d in data:
    try:
        e.append(float(d))
        count += 1
        total += float(d)
    except ValueError:
        print("跳過:",d)
print(f"有效{count}筆,平均:{total/count:.2f}")