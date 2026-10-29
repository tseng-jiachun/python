import pandas as pd

df=pd.read_csv("sensors.csv")
print("筆數: ",len(df))
print("平均溫度: ",df["temp"].mean())
print("最高溫度: ",df["temp"].max())

