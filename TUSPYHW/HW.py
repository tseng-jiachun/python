a=int(input("輸入正整數："))
a=bin(a)
print(f"原始二進位: {a[2:]}")
b=[i for i in a[2:]]
b.reverse()
print(f"反轉二進位: {''.join(i for i in b)}")
if a[2:]!=''.join(i for i in b):
      print("是否回文數: FALSE")
else:
      print("是否回文數: TRUE")
